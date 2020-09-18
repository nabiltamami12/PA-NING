<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Home Page</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,600" rel="stylesheet">

        <!-- Styles -->
        <style> 
            html, body {
                width: 100%;
                height: 400px;
                background-image: url("latar.png");
                background-size: 100% 100%;
                color: #636b6f;
                font-family: 'Nunito', sans-serif;
                font-weight: 200;
                height: 100vh;
                margin: 0;
            }

            .full-height {
                height: 100vh;
            }

            .flex-center {
                align-items: center;
                display: flex;
                justify-content: center;
            }

            .position-ref {
                position: relative;
            }

            /*.top-right {
                position: absolute;
                right: 10px;
                top: 18px;
            }*/

            .content {
                text-align: center;
            }

            .title {
                font-size: 84px;s
            }

            .links > a {
                color: white;
                padding: 30px;  /*jarak antar kata*/
                font-size: 20px; 
                font-weight: 600;  /*ketebalan huruf*/
                letter-spacing: .2rem; /*jarak antar huruf*/
                text-decoration: none;
                text-transform: uppercase;
            }

          /*  .m-b-md {
                padding: 120px; jarak antara gambar dan tulisan
            }
            */
        </style>
    </head> 
    <body background = "Home page.png" >
        <div class="flex-center position-ref full-height">

            <div class="content">

                <div style="padding: 150px;">
                    <img src="bri.gif" height= "140px" width="260" style="padding: 30px;"/>
                    <img src="bca.png" height= "140px" width="260" style="padding: 30px;"/>
                    <img src="BTN.jpg" height= "140px" width="260" style="padding: 30px;"/>
                </div>

                <div class="links">
                    @auth
                        <a href="{{ url('/home') }}">Home</a>
                    @else
                        <a href="{{ route('login') }}">Login</a>

                        @if (Route::has('register'))
                            <a href="{{ route('register') }}">Register</a>
                        @endif
                    @endauth
                </div>

            </div>
        </div>
    </body>
</html>
