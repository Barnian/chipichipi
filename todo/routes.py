from fastapi import Request, Depends, Form
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND
from pydantic import BaseModel, EmailStr
from todo.config import settings
# from todo.database.base import get_db
from todo.app import app, templates
# from todo.models import ToDo

class Title(BaseModel):
    title: str

class SignUp(BaseModel):
    email: str
    psw: str


# @app.get('/')
# def home(request: Request, db_session: Session = Depends(get_db)):
#     todos = db_session.query(ToDo).all()
#     return templates.TemplateResponse('todo/index.html',
#                                       {'request': request,
#                                        'app_name': settings.app_name,
#                                        'todo_list': todos}
#                                       )

text = """

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sit amet dapibus diam. Interdum et malesuada fames ac ante ipsum primis in faucibus. Morbi elementum dui ex, vel gravida risus sodales a. Proin ultricies elit diam, nec fermentum elit laoreet nec. Sed nisl tellus, ornare ut elit vitae, sagittis molestie ligula. Duis vitae turpis non sem hendrerit fringilla. Suspendisse interdum felis id neque finibus congue. Phasellus luctus nec velit vel vehicula. Aliquam et porta dui. Vivamus pretium nec lacus in vestibulum. Etiam et orci hendrerit, pharetra massa nec, volutpat nulla. In hac habitasse platea dictumst.

Aenean quis fringilla purus. Ut sed mauris at sem lobortis efficitur. Curabitur blandit lacinia efficitur. Fusce metus nibh, dignissim vel leo vel, ornare pharetra nunc. Fusce lacus urna, lobortis in orci eu, lacinia pretium sapien. Proin nec libero rutrum, cursus odio in, semper odio. Etiam commodo augue ac turpis fringilla, at congue urna porttitor. Aliquam non tempor eros, ut varius ligula. Morbi vestibulum nunc ac vestibulum consectetur. Integer eu est ex. Mauris volutpat justo eget varius scelerisque. Etiam eget tempus orci, imperdiet porttitor leo. Pellentesque dapibus vulputate lorem sit amet bibendum. Duis lobortis feugiat tellus, et fringilla metus tempor id. Nam blandit mollis eros sed luctus.

Donec quam eros, maximus vel metus quis, porta sagittis odio. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam erat volutpat. Cras vel erat cursus, blandit velit vel, facilisis dolor. Aenean imperdiet ultricies placerat. Nam eget nunc ac dui dignissim auctor. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque ut dapibus lorem. Nam massa orci, eleifend at est at, laoreet hendrerit quam. Vivamus eu turpis vel tortor scelerisque euismod. Donec faucibus nisl quis elit auctor, a sagittis ante dignissim. Maecenas id ipsum eget nisl pharetra commodo id id magna. Etiam et hendrerit nibh, ut faucibus odio. Suspendisse sapien magna, tempus in ullamcorper vel, laoreet non ipsum. Fusce fermentum eget urna tempor congue.

Vestibulum non purus elit. Nullam rhoncus sit amet velit nec semper. Nulla facilisi. Sed id eleifend nulla. Fusce dignissim vestibulum lacinia. Aenean in malesuada nisi. Etiam odio odio, semper et convallis et, pellentesque viverra arcu. Aenean tincidunt fermentum turpis, eget euismod justo consequat non. Aenean a finibus sem. Duis ultricies tellus justo, a sollicitudin arcu viverra non. Vivamus pellentesque sed neque sit amet facilisis. Nam vulputate nisl mauris, ullamcorper elementum augue molestie a. Nullam facilisis consectetur mattis. Maecenas turpis leo, dignissim a rutrum sit amet, volutpat a dui. Aliquam erat volutpat.

Nulla et nulla sit amet tortor congue ullamcorper. Aliquam erat volutpat. Donec vestibulum pharetra varius. Pellentesque sit amet neque vitae sapien tincidunt bibendum ac porttitor sapien. Mauris pharetra feugiat turpis, non scelerisque tellus dictum ac. Nam fermentum ligula sit amet mauris ultricies commodo non nec metus. Phasellus vitae lacus eu orci suscipit maximus id at ante. Vivamus fringilla in augue in venenatis. Ut dictum erat risus, sit amet tempor felis pharetra nec. Duis consequat pulvinar metus pretium varius. """

@app.get('/')
def home(request: Request):
    # todos = db_session.query(ToDo).all()
    chapters = [["https://google.com", "Введение"], ["https://google.com", "китвй"], ["https://google.com", "ноготочки"], ["https://google.com", "ршифин"]]
    author = "Алина Пермякова"
    author_description = "WebStorm позволяет сэкономить массу времени на часто повторяющихся действиях. Почти для всех таких действий существуют сочетания клавиш. Запомнить все эти сочетания невозможно, но в этом и нет необходимости. Предлагаем вам для начала освоить основные из них, и вы сразу увидите, насколько быстрее и эффективнее вы будете работать."

    return templates.TemplateResponse('todo/index.html',
                                      {'request': request,
                                       "chapters": chapters,
                                       "author_description": author_description,
                                        'author': author,
                                       "avatar": "../static/image/mine.jpg",
                                       'text': text}

                                      )

@app.get('/create_title')
def home(request: Request):
    return templates.TemplateResponse('todo/articleredact.html',
                                      {'request': request,
                                       })
    pass

@app.get('/auth')
def home(request: Request):
    return templates.TemplateResponse('todo/authpage.html',
                                      {'request': request,
                                       })
    pass

@app.post('/authentification')
def add(sig: SignUp):
    # new_todo = ToDo(title=title)
    # db_session.add(new_todo)
    # db_session.commit()
    print(sig.email, sig.psw)
    # url = app.url_path_for('home')
    # return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)



@app.post('/add')
def add(title: Request):
    # new_todo = ToDo(title=title)
    # db_session.add(new_todo)
    # db_session.commit()
    print(str(title))
    # url = app.url_path_for('home')
    # return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)

#
# @app.get('/update/{todo_id}')
# def update(todo_id: int, db_session: Session = Depends(get_db)):
#     todo = db_session.query(ToDo).filter(ToDo.id == todo_id).first()
#     todo.is_complete = not todo.is_complete
#     db_session.commit()
#
#     url = app.url_path_for('home')
#
#     return RedirectResponse(url=url, status_code=HTTP_302_FOUND)
#
#
# @app.get('/delete/{todo_id}')
# def delete(todo_id: int, db_session: Session = Depends(get_db)):
#     todo = db_session.query(ToDo).filter_by(id=todo_id).first()
#     db_session.delete(todo)
#     db_session.commit()
#
#     url = app.url_path_for('home')
#     return RedirectResponse(url=url, status_code=HTTP_302_FOUND)
