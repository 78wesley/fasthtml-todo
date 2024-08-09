from fasthtml.common import *


def render(todo):
    tid = f"todo-{todo.id}"
    toggle = A("Toggle", hx_post=f"/todo/{todo.id}/toggle", target_id=tid)
    edit = A("Edit", hx_get=f"/todo/{todo.id}/edit", hx_swap="this", target_id=tid)
    text = Span(todo.title)
    return Li(Span("✅" if todo.done else "❌"), toggle, edit, text, id=tid)


def todo_input():
    return Input(
        placeholder="Add a new todo", id="title", hx_swap_oob="true", required=""
    )

def head():
    return (Script(src='https://cdn.jsdelivr.net/npm/admin-lte@3.1/dist/js/adminlte.min.js'),
Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/admin-lte@3.1/dist/css/adminlte.min.css'))

app, route, todos, Todo = fast_app(
    db="todos.db", live=True, render=render, id=int, title=str, done=bool, pk="id", pico=False, hdrs=head()
)

import first as fr

@route("/")
def get():
    form = Form(
        Group(todo_input(), Button("Add")),
        hx_post="/todo",
        target_id="todo-list",
        hx_swap="beforeend",
    )

    return fr.first()
    # return Titled(
    #     "Todos", Card(Ul(*todos(), id="todo-list", hx_swap="outerHTML"), header=form)
    # )


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
def post(todo: Todo): # type: ignore
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
