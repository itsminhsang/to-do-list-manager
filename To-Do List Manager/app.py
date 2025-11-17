from flask import Flask, render_template, request, redirect, url_for
from db import db
from models import Todo, Category
from datetime import datetime
from flask import jsonify

app = Flask(__name__)

# ⚙️ Cấu hình MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/todo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#  Gắn SQLAlchemy vào app Flask
db.init_app(app)

#  Tạo bảng nếu chưa có
with app.app_context():
    db.create_all()


#  Trang chính
@app.route('/')
def index():
    filter_by = request.args.get('filter', 'all')
    category_id = request.args.get('category')

    query = Todo.query

    if category_id:
        query = query.filter_by(category_id=category_id)
    elif filter_by == 'active':
        query = query.filter_by(completed=False)
    elif filter_by == 'completed':
        query = query.filter_by(completed=True)

    todos = query.order_by(Todo.created_at.desc()).all()
    categories = Category.query.all()

    stats = {
        'total': Todo.query.count(),
        'active': Todo.query.filter_by(completed=False).count(),
        'completed': Todo.query.filter_by(completed=True).count(),
    }

    return render_template(
        'index.html',
        todos=todos,
        categories=categories,
        stats=stats,
        filter_by=filter_by,
        selected_category=category_id
    )


# ➕ Thêm công việc
@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    description = request.form.get('description')
    priority = request.form.get('priority', 'medium')
    category_id = request.form.get('category_id')
    due_date_str = request.form.get('due_date')

    due_date = None
    if due_date_str:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d')

    new_todo = Todo(
        title=title,
        description=description,
        priority=priority,
        category_id=category_id or None,
        due_date=due_date
    )

    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


# Xóa công việc
@app.route('/delete/<int:id>')
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


#  Sửa công việc
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_todo(id):
    todo = Todo.query.get_or_404(id)
    categories = Category.query.all()

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form.get('description')
        todo.priority = request.form.get('priority', 'medium')
        todo.category_id = request.form.get('category_id') or None
        due_date_str = request.form.get('due_date')

        todo.due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', todo=todo, categories=categories)


# ✅ Toggle trạng thái hoàn thành
@app.route('/toggle/<int:id>')
def toggle_todo(id):
    todo = Todo.query.get_or_404(id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('index'))


#  Trang quản lý danh mục
@app.route('/categories')
def manage_categories():
    categories = Category.query.all()
    return render_template('manage_categories.html', categories=categories)


#  Thêm danh mục
@app.route('/add_category', methods=['POST'])
def add_category():
    name = request.form['name']
    color = request.form.get('color', '#667eea')

    new_category = Category(name=name, color=color)
    db.session.add(new_category)
    db.session.commit()
    return redirect(url_for('manage_categories'))


# Xóa danh mục
@app.route('/delete_category/<int:id>')
def delete_category(id):
    category = Category.query.get_or_404(id)

    # Xóa tất cả todo thuộc danh mục này (nếu có)
    todos = Todo.query.filter_by(category_id=id).all()
    for t in todos:
        db.session.delete(t)

    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('manage_categories'))



if __name__ == '__main__':
    app.run(debug=True)
