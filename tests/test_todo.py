from endpoints.Todo import Todo

def test_create_todo(user, token):
    # This test creates a new user, creates a new todo_.
    todo = Todo(token)
    result = todo.CreateTodo(user)
    assert "Todo added!" in result

def test_get_all_todos(token):
    # This test creates a new user, retrieves all the todo_ items
    todo = Todo(token)
    result = todo.GetAllTodoItems()
    assert "There are no todo items currently waiting to be done!" in result

def test_delete_todos(user, token):
    # This test creates a new user, creates a new todo_ item, and then deletes the todo_.
    todo = Todo(token)
    result = todo.DeleteTodo(user)
    assert "Todo deleted" in result

