from fasthtml.common import *
import first as fr
from hmac import compare_digest


def todo_input():
    return Input(placeholder="Add a new todo", id="title", hx_swap_oob="true", required="")


def head():
    return (
        Meta(name="color-scheme", content="dark"),
        # Script(src="https://cdn.jsdelivr.net/npm/admin-lte@3.1/dist/js/adminlte.min.js"),
        # Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/admin-lte@3.1/dist/css/adminlte.min.css"),
        SortableJS(".sortable"),
        picolink,
    )


login_redir = RedirectResponse("/login", status_code=303)


def before(req, sess):
    auth = req.scope["auth"] = sess.get("auth", None)
    if not auth:
        return login_redir
    todos.xtra(name=auth)


db = database("todos.db")
todos, users = db.t.todos, db.t.users
if todos not in db.t:
    users.create(dict(name=str, pwd=str), pk="name")
    todos.create(id=int, title=str, done=bool, name=str, details=str, priority=int, pk="id")
Todo, User = todos.dataclass(), users.dataclass()


def _not_found(req, exc):
    return Titled("Oh no!", Div("We could not find that page :("))


beforeware = Beforeware(before, skip=[r"/favicon\.ico", "/login"])
app = FastHTML(before=beforeware, exception_handlers={404: _not_found}, live=True, hdrs=head())
route = app.route


@route("/login")
def get():
    form = Form(
        Input(id="name", placeholder="Name"),
        Input(id="pwd", type="password", placeholder="Password"),
        Button("Login"),
        action="/login",
        method="post",
    )
    return Titled("Login", (Div(form)))


@dataclass
class Login:
    name: str
    pwd: str


@route("/login")
def post(login: Login, sess):
    if not login.name or not login.pwd:
        return login_redir
    try:
        u = users[login.name]
    except NotFoundError:
        u = users.insert(login)
    if not compare_digest(u.pwd.encode("utf-8"), login.pwd.encode("utf-8")):
        return login_redir
    sess["auth"] = u.name
    return RedirectResponse("/", status_code=303)


@app.get("/logout")
def logout(sess):
    del sess["auth"]
    return login_redir


@patch
def __ft__(self: Todo):
    tid = f"todo-{self.id}"
    toggle = A("Toggle", hx_post=f"/todo/{self.id}/toggle", target_id=tid)
    edit = A("Edit", hx_get=f"/todo/{self.id}/edit", hx_swap="this", target_id=tid)
    text = Span(self.title)
    return Li(Span("✅" if self.done else "❌"), toggle, edit, text, id=tid)


@route("/")
def get(auth):
    title = f"{auth}'s Todo list"
    top = Grid(H1(title), Div(A("Logout", href="/logout", role="button", cls="secondary"), style="text-align: right"))
    form = Form(
        Group(todo_input(), Button("Add")),
        hx_post="/todo",
        target_id="todo-list",
        hx_swap="beforeend",
    )
    card = Card(Ul(*todos(order_by="priority"), id="todo-list", cls="sortable", hx_swap="outerHTML"), header=form)

    return Title(title), Container(top, card)


@route("/todo/{tid}/edit")
def get(tid: int):
    todo = todos[tid]
    return Form(
        Group(
            Input(id="title", required="", value=todo.title),
            Button("Update"),
            Button("Delete", hx_delete=f"/todo/{tid}", hx_params="none", target_id=f"todo-{tid}"),
            Button("Cancel", hx_get=f"/todo/{tid}", cls="secondary", target_id=f"todo-{tid}"),
            style="margin-top: var(--pico-spacing)",
        ),
        hx_put=f"/todo/{tid}",
    )


@route("/todo/{tid}")
def get(tid: int):
    todo = todos[tid]
    return render(todo)


@route("/todo/{tid}")
def put(tid: int, title: str):
    todo = todos[tid]
    todo.title = title
    return todos.update(todo)


@route("/todo")
def post(todo: Todo):  # type: ignore
    return todos.insert(todo), todo_input()


@route("/todo/{tid}/toggle")
def post(tid: int):
    todo = todos[tid]
    todo.done = not todo.done
    return todos.update(todo)


@route("/todo/{tid}")
def delete(tid: int):
    todos.delete(tid)


serve()
