# FlaskBlog
a blog built by flask

markdown.js无法渲染markdown表格
解决：markdown.js文件982行`return '<table>\n'`修改为`return '<table class="table table-hover">\n'`
在app/static/css中添加rainbow.css文件
在app/static/js中添加markded.js和highlight.pack.js文件
还未解决的问题：markdown中插入图片的路径问题
