from nicegui import ui,app


def render():
    # big container
    with ui.element("nav").classes("flex flex-row justify-between items-center w-full fixed bg-white left-0 top-0 px-6 py-4 shadow-md z-50"):
        # logo
        ui.label("ElizaFood").classes("font-lobster text-2xl text-orange-500")

        # navlinks
        navlinks = [
            {"title": "Home", "path": "/"},
            {"title": "Menu", "path": "/menu"},
            {"title": "About", "path": "/about"},
            {"title": "Gallery", "path": "/gallery"},
            {"title": "Blog", "path": "/blog"},
            {"title": "Contact", "path": "/contact"}
        ]
        with ui.row().classes("gap-6"):
            for item in navlinks:
                ui.link(item["title"], item["path"]).classes(
                    "no-underline uppercase text-black font-semibold hover:text-orange-500"
                )

        # socials
        with ui.row().classes("gap-4 text-xl text-orange-500"):
            ui.html('<i class="fa-solid fa-cart-shopping"></i>')

    # hero section
    with ui.element("div").classes("w-full h-screen"): 
        with ui.element("div").style(
            "background-image:url('https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg'); "
            "background-size:cover; background-repeat:no-repeat; background-position:center;"
        ).classes("w-full h-full flex flex-col justify-center items-center"):
            
            with ui.element("div").style(
    "background: linear-gradient(to bottom, rgba(0,0,0,0.2), rgba(0,0,0,0.6));").classes("absolute inset-0"):
                pass
            
            # text 
            with ui.element("div").classes("relative text-center font-bold drop-shadow-lg"):
                ui.label("Welcome to").classes("text-4xl font-lobster  text-black-100 mb-4")

                with ui.element("div").classes("flex flex-row justify-center gap-2 mb-6"):
                    ui.label("Eliza").classes("text-7xl text-white")
                    ui.label("Foods").classes("text-7xl text-orange-500")

                ui.button("Look Menu").props("dense flat no-caps").classes(
                    "bg-white hover:bg-orange-400 text-orange px-6 py-3 rounded-lg"
                )

