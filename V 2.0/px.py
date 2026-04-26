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
    b=deepseek2("""
    你是一个生成图片的AI,你要生成图片，10px*10px,
    你要这样做:
    0=black
    1=white
    2=red 
    3=orange
    4=yellow
    5=lime
    6=green
    7=blue
    8=purple
    要根据用户的要求生成相应图片,你在(:: ::)这个特殊符号里面回答图片code,e.g#1:用户:做一个一半黑一半白的图片,you:
    (::0000011111 0000011111 00000111111 0000011111 0000011111 0000011111 0000011111 0000011111 0000011111 0000011111::)
    为什么要回答这个呢？因为会自动把里面的内容把空格替换成换行,还会再把零替换成黑色像素点，然后呢一替换成白色像素点。:
    0000011111
    0000011111
    0000011111
    0000011111
    0000011111
    0000011111
    0000011111
    0000011111
    0000011111
    0000011111
    这样这个数字就成为了10px*10px一半黑一半白的图像了,
    e.g#2:用户:做一个中间有黑方块儿的图片，背景为白色,you:
    (::1111111111 1100000011 1100000011 1100000011 1100000011 1100000011 1100000011 1100000011 1100000011 1111111111::)
    为什么要回答这个呢？因为会自动把里面的内容把空格替换成换行,还会再把零替换成黑色像素点，然后呢一替换成白色像素点。:
    1111111111
    1100000011
    1100000011
    1100000011
    1100000011
    1100000011
    1100000011
    1100000011
    1100000011
    1111111111
    这样这个数字就成为了图像了,如果用户要求你不一定是白色，中间有一个黑色方块儿的图，而是其他颜色，如果用户没明确说是在左下角或右下角有个方块儿，那你就要改一下那个:
    e.g:
    用户:做一个中间有蓝色方块儿的图片，背景为黑色,you:
    (::0000000000 0077777700 0077777700 0077777700 0077777700 0077777700 0077777700 0077777700 0077777700 0000000000::)
    如果用户明确要求说是左下角或右下角，你就要按照他说的生成就够了。
    如果用户让你生成复杂的图形，比如爱心，你就按照它的生成，严格按照我出的格式，在这里我用x代表用户的心形颜色，用y代表用户想要的背景颜色，你的任务就是将x替换成用户要求的心形颜色的数字,将y替换成用户要求的背景颜色数字,你只用做这一件事就够了：
    yyyyyyyyyy
    yyyyyyyyyy
    yxxxyyxxxy
    xxxxxxxxxx
    yxxxxxxxxy
    yyxxxxxxyy
    yyyxxxxyyy
    yyyyxxyyyy
    yyyyyyyyyy
    yyyyyyyyyy
    严格按照我的要求,让图形对称,不要生成不对称的心,
    e.g:用户:生成green的心，黑色的背景。,you:
    (::0000000000 0000000000 0666006660 6666666666 0666666660 0066666600 0006666000 0000660000 0000000000 0000000000::)
    你就要像这样完整的替换x，不要改格式，不要改成这样：
    (::1111111111 1111111111 1555511555 5555555555 1555555551 1155555511 1115555111 1111551111 1111111111 1111111111::)
    因为这里的第三行1555511555没有正确的替换,正确的替换应该是1555115551，这样就不符合格式了。以后不许有这种不符合格式的图片。
    并且每行要有10个数字,不要有11个或9个或其他的只能这10个每一行,而且总共只能有10：  
    (::1111111111 1100000011 1100000011 1100000011 1100000011 1100000011 1100000011 1100000011 1100000011 1111111111::)
    你要生成像这样的，不管是生成一个爱心还是一个方块儿，都要尊这种格式，不能像这样(::1111111111 1111111111 16666116661 6666666666 16666666661 11666666611 11166666111 11116611111 1111111111 1111111111::)
    这样每个就有11个字符了。
    你就根据用户的要求回答这些像素数字就可以生成图片。这里是用户的要求:
    """+a)
    c=b.split("(::")[1].split("::)")[0]
    return """    
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>IMG plus</title>
    <style>
        /* 统一基础样式 */
        div {
            position: absolute;
            width: 10%;
            height: 10%;
        }

        /* —————————— 超长独立定位 CSS 开始 —————————— */

        /* 第1行 a1 - a10 */
        #a1 { top: 0%; left: 0%; }
        #a2 { top: 0%; left: 10%; }
        #a3 { top: 0%; left: 20%; }
        #a4 { top: 0%; left: 30%; }
        #a5 { top: 0%; left: 40%; }
        #a6 { top: 0%; left: 50%; }
        #a7 { top: 0%; left: 60%; }
        #a8 { top: 0%; left: 70%; }
        #a9 { top: 0%; left: 80%; }
        #a10 { top: 0%; left: 90%; }

        /* 第2行 a11 - a20 */
        #a11 { top: 10%; left: 0%; }
        #a12 { top: 10%; left: 10%; }
        #a13 { top: 10%; left: 20%; }
        #a14 { top: 10%; left: 30%; }
        #a15 { top: 10%; left: 40%; }
        #a16 { top: 10%; left: 50%; }
        #a17 { top: 10%; left: 60%; }
        #a18 { top: 10%; left: 70%; }
        #a19 { top: 10%; left: 80%; }
        #a20 { top: 10%; left: 90%; }

        /* 第3行 a21 - a30 */
        #a21 { top: 20%; left: 0%; }
        #a22 { top: 20%; left: 10%; }
        #a23 { top: 20%; left: 20%; }
        #a24 { top: 20%; left: 30%; }
        #a25 { top: 20%; left: 40%; }
        #a26 { top: 20%; left: 50%; }
        #a27 { top: 20%; left: 60%; }
        #a28 { top: 20%; left: 70%; }
        #a29 { top: 20%; left: 80%; }
        #a30 { top: 20%; left: 90%; }

        /* 第4行 a31 - a40 */
        #a31 { top: 30%; left: 0%; }
        #a32 { top: 30%; left: 10%; }
        #a33 { top: 30%; left: 20%; }
        #a34 { top: 30%; left: 30%; }
        #a35 { top: 30%; left: 40%; }
        #a36 { top: 30%; left: 50%; }
        #a37 { top: 30%; left: 60%; }
        #a38 { top: 30%; left: 70%; }
        #a39 { top: 30%; left: 80%; }
        #a40 { top: 30%; left: 90%; }

        /* 第5行 a41 - a50 */
        #a41 { top: 40%; left: 0%; }
        #a42 { top: 40%; left: 10%; }
        #a43 { top: 40%; left: 20%; }
        #a44 { top: 40%; left: 30%; }
        #a45 { top: 40%; left: 40%; }
        #a46 { top: 40%; left: 50%; }
        #a47 { top: 40%; left: 60%; }
        #a48 { top: 40%; left: 70%; }
        #a49 { top: 40%; left: 80%; }
        #a50 { top: 40%; left: 90%; }

        /* 第6行 a51 - a60 */
        #a51 { top: 50%; left: 0%; }
        #a52 { top: 50%; left: 10%; }
        #a53 { top: 50%; left: 20%; }
        #a54 { top: 50%; left: 30%; }
        #a55 { top: 50%; left: 40%; }
        #a56 { top: 50%; left: 50%; }
        #a57 { top: 50%; left: 60%; }
        #a58 { top: 50%; left: 70%; }
        #a59 { top: 50%; left: 80%; }
        #a60 { top: 50%; left: 90%; }

        /* 第7行 a61 - a70 */
        #a61 { top: 60%; left: 0%; }
        #a62 { top: 60%; left: 10%; }
        #a63 { top: 60%; left: 20%; }
        #a64 { top: 60%; left: 30%; }
        #a65 { top: 60%; left: 40%; }
        #a66 { top: 60%; left: 50%; }
        #a67 { top: 60%; left: 60%; }
        #a68 { top: 60%; left: 70%; }
        #a69 { top: 60%; left: 80%; }
        #a70 { top: 60%; left: 90%; }

        /* 第8行 a71 - a80 */
        #a71 { top: 70%; left: 0%; }
        #a72 { top: 70%; left: 10%; }
        #a73 { top: 70%; left: 20%; }
        #a74 { top: 70%; left: 30%; }
        #a75 { top: 70%; left: 40%; }
        #a76 { top: 70%; left: 50%; }
        #a77 { top: 70%; left: 60%; }
        #a78 { top: 70%; left: 70%; }
        #a79 { top: 70%; left: 80%; }
        #a80 { top: 70%; left: 90%; }

        /* 第9行 a81 - a90 */
        #a81 { top: 80%; left: 0%; }
        #a82 { top: 80%; left: 10%; }
        #a83 { top: 80%; left: 20%; }
        #a84 { top: 80%; left: 30%; }
        #a85 { top: 80%; left: 40%; }
        #a86 { top: 80%; left: 50%; }
        #a87 { top: 80%; left: 60%; }
        #a88 { top: 80%; left: 70%; }
        #a89 { top: 80%; left: 80%; }
        #a90 { top: 80%; left: 90%; }

        /* 第10行 a91 - a100 */
        #a91 { top: 90%; left: 0%; }
        #a92 { top: 90%; left: 10%; }
        #a93 { top: 90%; left: 20%; }
        #a94 { top: 90%; left: 30%; }
        #a95 { top: 90%; left: 40%; }
        #a96 { top: 90%; left: 50%; }
        #a97 { top: 90%; left: 60%; }
        #a98 { top: 90%; left: 70%; }
        #a99 { top: 90%; left: 80%; }
        #a100 { top: 90%; left: 90%; }

    </style>
    </head>
    <body>

    <!-- 100个div，id=a1 到 a100 -->
    <div id="a1"></div>
    <div id="a2"></div>
    <div id="a3"></div>
    <div id="a4"></div>
    <div id="a5"></div>
    <div id="a6"></div>
    <div id="a7"></div>
    <div id="a8"></div>
    <div id="a9"></div>
    <div id="a10"></div>

    <div id="a11"></div>
    <div id="a12"></div>
    <div id="a13"></div>
    <div id="a14"></div>
    <div id="a15"></div>
    <div id="a16"></div>
    <div id="a17"></div>
    <div id="a18"></div>
    <div id="a19"></div>
    <div id="a20"></div>

    <div id="a21"></div>
    <div id="a22"></div>
    <div id="a23"></div>
    <div id="a24"></div>
    <div id="a25"></div>
    <div id="a26"></div>
    <div id="a27"></div>
    <div id="a28"></div>
    <div id="a29"></div>
    <div id="a30"></div>

    <div id="a31"></div>
    <div id="a32"></div>
    <div id="a33"></div>
    <div id="a34"></div>
    <div id="a35"></div>
    <div id="a36"></div>
    <div id="a37"></div>
    <div id="a38"></div>
    <div id="a39"></div>
    <div id="a40"></div>

    <div id="a41"></div>
    <div id="a42"></div>
    <div id="a43"></div>
    <div id="a44"></div>
    <div id="a45"></div>
    <div id="a46"></div>
    <div id="a47"></div>
    <div id="a48"></div>
    <div id="a49"></div>
    <div id="a50"></div>

    <div id="a51"></div>
    <div id="a52"></div>
    <div id="a53"></div>
    <div id="a54"></div>
    <div id="a55"></div>
    <div id="a56"></div>
    <div id="a57"></div>
    <div id="a58"></div>
    <div id="a59"></div>
    <div id="a60"></div>

    <div id="a61"></div>
    <div id="a62"></div>
    <div id="a63"></div>
    <div id="a64"></div>
    <div id="a65"></div>
    <div id="a66"></div>
    <div id="a67"></div>
    <div id="a68"></div>
    <div id="a69"></div>
    <div id="a70"></div>

    <div id="a71"></div>
    <div id="a72"></div>
    <div id="a73"></div>
    <div id="a74"></div>
    <div id="a75"></div>
    <div id="a76"></div>
    <div id="a77"></div>
    <div id="a78"></div>
    <div id="a79"></div>
    <div id="a80"></div>

    <div id="a81"></div>
    <div id="a82"></div>
    <div id="a83"></div>
    <div id="a84"></div>
    <div id="a85"></div>
    <div id="a86"></div>
    <div id="a87"></div>
    <div id="a88"></div>
    <div id="a89"></div>
    <div id="a90"></div>

    <div id="a91"></div>
    <div id="a92"></div>
    <div id="a93"></div>
    <div id="a94"></div>
    <div id="a95"></div>
    <div id="a96"></div>
    <div id="a97"></div>
    <div id="a98"></div>
    <div id="a99"></div>
    <div id="a100"></div>
    <script>
		function A(){
			let a="""+"\""+c+"\""+""";
            let b=a.split(" ");
            let c=b.length-1;
            let num=1;
            for(let i=0;i<=c;i++){
                let d=b[i];
				let f=d.split("");
				let e=f.length-1;
				for(let r=0;r<=e;r++){
                    let g=f[r];
					if(g==="0"){
						document.getElementById("a"+String(num)).style.background="black";
					}else if(g==="1"){
						document.getElementById("a"+String(num)).style.background="white";
					}else if(g==="2"){
						document.getElementById("a"+String(num)).style.background="red";
					}else if(g==="3"){
						document.getElementById("a"+String(num)).style.background="orange";
					}else if(g==="4"){
						document.getElementById("a"+String(num)).style.background="yellow";
					}else if(g==="5"){
						document.getElementById("a"+String(num)).style.background="lime";
					}else if(g==="6"){
						document.getElementById("a"+String(num)).style.background="green";
					}else if(g==="7"){
						document.getElementById("a"+String(num)).style.background="blue";
					}else{
						document.getElementById("a"+String(num)).style.background="purple";
					}
					num++;
                }
            }
		}
		A();
	</script>
    </body>
    </html>
    """
go(28282)
