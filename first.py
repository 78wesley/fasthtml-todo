from fasthtml.common import *


def create_navbar():
    return Nav(
        Ul(
            create_navbar_items(),
            cls="navbar-nav",
        ),
        Ul(
            create_navbar_right_items(),
            cls="navbar-nav ml-auto",
        ),
        cls="main-header navbar navbar-expand navbar-white navbar-light",
    )


def create_navbar_items():
    return (
        Li(
            A(
                I(cls="fas fa-bars"),
                data_widget="pushmenu",
                href="#",
                role="button",
                cls="nav-link",
            ),
            cls="nav-item",
        ),
        Li(
            A("Home", href="index3.html", cls="nav-link"),
            cls="nav-item d-none d-sm-inline-block",
        ),
        Li(
            A("Contact", href="#", cls="nav-link"),
            cls="nav-item d-none d-sm-inline-block",
        ),
    )


def create_navbar_right_items():
    return (
        Li(
            create_search_item(),
            cls="nav-item",
        ),
        Li(
            create_messages_dropdown(),
            cls="nav-item dropdown",
        ),
        Li(
            create_notifications_dropdown(),
            cls="nav-item dropdown",
        ),
        Li(
            A(
                I(cls="fas fa-expand-arrows-alt"),
                data_widget="fullscreen",
                href="#",
                role="button",
                cls="nav-link",
            ),
            cls="nav-item",
        ),
        Li(
            A(
                I(cls="fas fa-th-large"),
                data_widget="control-sidebar",
                data_slide="true",
                href="#",
                role="button",
                cls="nav-link",
            ),
            cls="nav-item",
        ),
    )


def create_search_item():
    return (
        A(
            I(cls="fas fa-search"),
            data_widget="navbar-search",
            href="#",
            role="button",
            cls="nav-link",
        ),
        Div(
            Form(
                Div(
                    Input(
                        type="search",
                        placeholder="Search",
                        aria_label="Search",
                        cls="form-control form-control-navbar",
                    ),
                    Div(
                        Button(
                            I(cls="fas fa-search"),
                            type="submit",
                            cls="btn btn-navbar",
                        ),
                        Button(
                            I(cls="fas fa-times"),
                            type="button",
                            data_widget="navbar-search",
                            cls="btn btn-navbar",
                        ),
                        cls="input-group-append",
                    ),
                    cls="input-group input-group-sm",
                ),
                cls="form-inline",
            ),
            cls="navbar-search-block",
        ),
    )


def create_messages_dropdown():
    return A(
        I(cls="far fa-comments"),
        Span("3", cls="badge badge-danger navbar-badge"),
        data_toggle="dropdown",
        href="#",
        cls="nav-link",
    ), Div(
        create_message_items(),
        cls="dropdown-menu dropdown-menu-lg dropdown-menu-right",
    )


def create_message_items():
    return (
        create_message_item(
            "Brad Diesel", "Call me whenever you can...", "4 Hours Ago", "text-danger"
        ),
        Div(cls="dropdown-divider"),
        create_message_item(
            "John Pierce", "I got your message bro", "4 Hours Ago", "text-muted"
        ),
        Div(cls="dropdown-divider"),
        create_message_item(
            "Nora Silvester", "The subject goes here", "4 Hours Ago", "text-warning"
        ),
        Div(cls="dropdown-divider"),
        A("See All Messages", href="#", cls="dropdown-item dropdown-footer"),
    )


def create_message_item(name, message, time, star_class):
    return A(
        Div(
            Div(
                H3(
                    name,
                    Span(
                        I(cls="fas fa-star"),
                        cls=f"float-right text-sm {star_class}",
                    ),
                    cls="dropdown-item-title",
                ),
                P(message, cls="text-sm"),
                P(
                    I(cls="far fa-clock mr-1"),
                    time,
                    cls="text-sm text-muted",
                ),
                cls="media-body",
            ),
            cls="media",
        ),
        href="#",
        cls="dropdown-item",
    )


def create_notifications_dropdown():
    return A(
        I(cls="far fa-bell"),
        Span("15", cls="badge badge-warning navbar-badge"),
        data_toggle="dropdown",
        href="#",
        cls="nav-link",
    ), Div(
        create_notification_items(),
        cls="dropdown-menu dropdown-menu-lg dropdown-menu-right",
    )


def create_notification_items():
    return (
        Span("15 Notifications", cls="dropdown-header"),
        Div(cls="dropdown-divider"),
        create_notification_item("4 new messages", "3 mins", "fas fa-envelope mr-2"),
        Div(cls="dropdown-divider"),
        create_notification_item("8 friend requests", "12 hours", "fas fa-users mr-2"),
        Div(cls="dropdown-divider"),
        create_notification_item("3 new reports", "2 days", "fas fa-file mr-2"),
        Div(cls="dropdown-divider"),
        A(
            "See All Notifications",
            href="#",
            cls="dropdown-item dropdown-footer",
        ),
    )


def create_notification_item(description, time, icon):
    return A(
        I(cls=icon),
        description,
        Span(time, cls="float-right text-muted text-sm"),
        href="#",
        cls="dropdown-item",
    )


def create_sidebar():
    return Aside(
        A(
            Span("AdminLTE 3", cls="brand-text font-weight-light"),
            href="index3.html",
            cls="brand-link",
        ),
        Div(
            create_user_panel(),
            create_search_form(),
            create_nav_menu(),
            cls="sidebar",
        ),
        cls="main-sidebar sidebar-dark-primary elevation-4",
    )


def create_user_panel():
    return Div(
        Div(cls="image"),
        Div(A("Alexander Pierce", href="#", cls="d-block"), cls="info"),
        cls="user-panel mt-3 pb-3 mb-3 d-flex",
    )


def create_search_form():
    return Div(
        Div(
            Input(
                type="search",
                placeholder="Search",
                aria_label="Search",
                cls="form-control form-control-sidebar",
            ),
            Div(
                Button(I(cls="fas fa-search fa-fw"), cls="btn btn-sidebar"),
                cls="input-group-append",
            ),
            data_widget="sidebar-search",
            cls="input-group",
        ),
        Div(
            Div(
                A(
                    Div(
                        Strong(cls="text-light"),
                        "No",
                        Strong(cls="text-light"),
                        "ele",
                        Strong(cls="text-light"),
                        "ment",
                        Strong(cls="text-light"),
                        " found!",
                        cls="search-title",
                    ),
                    Div(cls="search-path"),
                    href="#",
                    cls="list-group-item",
                ),
                cls="list-group",
            ),
            cls="sidebar-search-results",
        ),
        cls="form-inline",
    )


def create_nav_menu():
    return Nav(
        Ul(
            create_nav_menu_items(),
            data_widget="treeview",
            role="menu",
            data_accordion="false",
            cls="nav nav-pills nav-sidebar flex-column",
        ),
        cls="mt-2",
    )


def create_nav_menu_items():
    return (
        Li(
            A(
                I(cls="nav-icon fas fa-tachometer-alt"),
                P("Starter Pages", I(cls="right fas fa-angle-left")),
                href="#",
                cls="nav-link active",
            ),
            Ul(
                create_submenu_items(),
                cls="nav nav-treeview",
            ),
            cls="nav-item menu-open",
        ),
        Li(
            A(
                I(cls="nav-icon fas fa-th"),
                P(
                    "Simple Link",
                    Span("New", cls="right badge badge-danger"),
                ),
                href="#",
                cls="nav-link",
            ),
            cls="nav-item",
        ),
    )


def create_submenu_items():
    return (
        Li(
            A(
                I(cls="far fa-circle nav-icon"),
                P("Active Page"),
                href="#",
                cls="nav-link active",
            ),
            cls="nav-item",
        ),
        Li(
            A(
                I(cls="far fa-circle nav-icon"),
                P("Inactive Page"),
                href="#",
                cls="nav-link",
            ),
            cls="nav-item",
        ),
    )


def create_header():
    return Div(
        Div(
            Div(
                Div(H1("Starter Page", cls="m-0"), cls="col-sm-6"),
                Div(
                    Ol(
                        Li(A("Home", href="#"), cls="breadcrumb-item"),
                        Li("Starter Page", cls="breadcrumb-item active"),
                        cls="breadcrumb float-sm-right",
                    ),
                    cls="col-sm-6",
                ),
                cls="row mb-2",
            ),
            cls="container-fluid",
        ),
        cls="content-header",
    )


def create_content():
    return Div(
        Div(
            Div(
                Div(
                    create_card(
                        "Card title",
                        "Some quick example text...",
                        "Card link",
                        "Another link",
                    ),
                    create_card(
                        "Card title",
                        "Some quick example text...",
                        "Card link",
                        "Another link",
                        card_class="card-primary card-outline",
                    ),
                    cls="col-lg-6",
                ),
                Div(
                    create_featured_card(
                        "Featured",
                        "Special title treatment",
                        "With supporting text below...",
                        "Go somewhere",
                    ),
                    create_featured_card(
                        "Featured",
                        "Special title treatment",
                        "With supporting text below...",
                        "Go somewhere",
                        card_class="card-primary card-outline",
                    ),
                    cls="col-lg-6",
                ),
                cls="row",
            ),
            cls="container-fluid",
        ),
        cls="content",
    )


def create_card(title, text, link1, link2, card_class: str = None):
    return Div(
        Div(
            H5(title, cls="card-title"),
            P(text, cls="card-text"),
            A(link1, href="#", cls="card-link"),
            A(link2, href="#", cls="card-link"),
            cls="card-body",
        ),
        cls=f"card {card_class}",
    )


def create_featured_card(header, title, text, button_text, card_class: str = None):
    return Div(
        Div(H5(header, cls="m-0"), cls="card-header"),
        Div(
            H6(title, cls="card-title"),
            P(text, cls="card-text"),
            A(button_text, href="#", cls="btn btn-primary"),
            cls="card-body",
        ),
        cls=f"card {card_class}",
    )


def create_footer():
    return Footer(
        Div("Anything you want", cls="float-right d-none d-sm-inline"),
        Strong(
            "Copyright © 2014-2021",
            A("AdminLTE.io", href="https://adminlte.io"),
            ".",
        ),
        "All rights reserved.",
        cls="main-footer",
    )


def create_aside():
    return Aside(
        Div(H5("Title"), P("Sidebar content"), cls="p-3"),
        style="display: none;",
        cls="control-sidebar control-sidebar-dark",
    )


def first():
    return Div(
        create_navbar(),
        create_sidebar(),
        Div(
            create_header(),
            create_content(),
            style="min-height: 1162px;",
            cls="content-wrapper",
        ),
        create_aside(),
        create_footer(),
        Div(id="sidebar-overlay"),
        cls="wrapper",
    )
