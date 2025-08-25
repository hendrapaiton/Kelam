from src.updates.email_update import update


def make_dispatch(model, render):
    def dispatch(event):
        nonlocal model
        model = update(model, event)
        render()
    return dispatch
