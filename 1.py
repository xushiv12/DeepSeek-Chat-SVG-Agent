from lib import *
@app.route("/")
def A():
    return render_template("1.html")
@app.route("/image-maker")
def B():
    return render_template("2.html")
@app.route("/AI")
def C():
    global a
    a=request.args.get("a")
    e=0
    b=deepseek2("""
    你是一个生成图片的AI,你要使用SVG来生成图片,别忘了你要在最开头的时候加
    <svg width="100%" height="100%" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
    在结尾的时候要加
    </svg>
    这是现成的白云图片:
    /static/1.png
    这是现成的蓝天图片:
    /static/2.png
    这是现成的猫的图片:
    /static/3.png
    这是现成的鸟的图片:
    /static/4.png
    这是现成的楼房图片:
    /static/5.png
    这是现成的狗的图片:
    /static/6.png
    这是现成的雨的图片:
    /static/7.png
    这是现成的男人的图片:
    /static/8.png
    这是现成的女人的图片:
    /static/9.png
    你要使用<image>标签来调用这些,e.g:
    用户:"生成一张蓝天白云的图片"
    <svg width="100%" height="100%" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
    <image href="/static/2.png" x="300" y="120" width="200" height="250" />
    <image href="/static/1.png" x="300" y="120" width="200" height="250" />
    </svg>
    你还需要分清什么是背景，什么是显示物，比如刚才的那个例子中,蓝天是背景，白云是显示物。
    还有就是如果用户让你生成一张男人走在雨中的图片,你也要分清哪个是背景，哪个是显示物，男人是显示物，雨是背景。
    记住背景和显示物的x,y,width,height都必须和刚才例子中的是一样的，x必须是300,y必须是120",width必须是200,
    height必须是250。如果用户让你生成一些简单的图片，比如画一个红色的圆，你就要使用svg里面原生的一些标签，比如<circle><rect><text><path>,如果用户想让你画一些东西，比如蓝天白云加圆圈，那你就先编刚才的那个蓝天白云的图片，然后呢在这上面画一个用原生标签页画一个像太阳的圆(<circle>)，如果用户要求的是月亮你要听用户要求的什么月亮，如果是弯弯的月亮就使用<path>画,如果是圆形的，那你就画用户要求颜色的圆形,如果用户要求的是其他图形，那你就在要求，比如男人走在雨中加一个爱心图案，那你就照着他的要求画先用<image>画出男人走在雨中，然后呢再在那张图案上加一个爱心就够了，如果用户要求加的是图库里已经有了，比如蓝天白云，再加个小鸟，那你只需要使用<image>。这是用户的提示词:
    """+a)
    c=b.split("""<svg width="100%" height="100%" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">""")[1].split("</svg>")[0]
    d="""<svg width="100%" height="100%" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">"""+c+"""</svg>"""
    return d
go(28282)