from nicegui import ui,app


def render():
    # big container
    with ui.element("div").classes("w-screen h-screen"):
        with ui.element("nav").classes("flex flex-row justify-between w-full fixed bg-white left-0 top-0 px-4 py-4"):
                # logo
                ui.label("ElizaFood").classes("font-bold text-2xl text-orange-400")
                # navlinks
                navlinks = [
                    {"title":"Home","path":"/"},
                    {"title":"Menu","path":"/"},
                    {"title":"About","path":"/"},
                    {"title":"Gallery","path":"/"},
                    {"title":"Blog","path":"/"},
                    {"title":"Contact","path":"/"}
                ]
                with ui.row():
                    for item in navlinks:
                        ui.link(item["title"], item["path"]).classes("no-underline uppercase text-black font-bold")
                
                # socials fac
                with ui.row().classes():
                    ui.html('<i class="fa-brands fa-square-facebook"></i>')
                    ui.html('<i class="fa-brands fa-instagram"></i>')
                    ui.html('<i class="fa-brands fa-x-twitter"></i>')
        
        with ui.element("div").style("background-image:url('https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg'); " \
        "background-size:cover; background-repeat: no-repeat; background-position: center;") \
            .classes("w-full h-full flex flex-col justify-center items-center"):        
            # text 
            with ui.element("div").classes("text-center font-bold"):
                ui.label("Welcome to").classes("text-4xl")
                
                with ui.element("div").classes("flex flex-row"):
                    ui.html("<h1>Eliza</h1>").classes("text-7xl")
                    ui.html("<h1>Foods</h1>").classes("text-7xl text-orange-600 mb-8")
                
                ui.button("Look Menu", color="orange-400").classes("hover:bg-orange-300 text-white")
