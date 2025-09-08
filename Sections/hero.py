from nicegui import ui,app


def render():
    # big container
    with ui.element("nav").classes("flex flex-row justify-between items-center w-full fixed bg-white left-0 top-0 px-10 py-4 shadow-md z-50"):
        # logo
        with ui.link(target="_self").classes("no-underline border-2 border-orange-500 rounded-lg pl-4 pr-4 text-center inline-block"):
            ui.label("GardenFresh").classes("font-Poppins font-bold text-black block")
            ui.label("Restaurant").classes("font-Poppins text-black block")

        # navlinks
        navlinks = [
            {"title": "Home", "path": "/"},
            {"title": "Menu", "path": "/menu"},
            {"title": "Reservation", "path": "/reservation"},
            {"title": "About", "path": "/about"},
            {"title": "Gallery", "path": "/gallery"},
            {"title": "Blog", "path": "/blog"},
            {"title": "Contact", "path": "/contact"}
        ]
        with ui.row().classes("gap-6"):
            for item in navlinks:
                ui.link(item["title"], item["path"]).classes(
                    "no-underline uppercase text-black font-Poppins hover:!text-orange-500 transition-colors duration-300"
                )


        # Add to cart
        with ui.button().props("dense flat no-caps").classes("rounded-full w-[75px] bg-orange-500"):
            with ui.link().classes("gap-4 text-l text-black text-center"):
                ui.html('<i class="fa-solid fa-cart-shopping"></i>')

    # hero section
    with ui.element("div").classes("w-full h-screen relative pt-[75px]"): 
        with ui.element("div").style(
            "background-image:url('https://images.pexels.com/photos/1640770/pexels-photo-1640770.jpeg'); "
            "background-size:cover; background-repeat:no-repeat; background-position:center;"
        ).classes("w-full h-full flex flex-col justify-center items-center"):
            
            with ui.element("div").style(
                "background: linear-gradient(to bottom, rgba(0,0,0,0.2), rgba(0,0,0,0.6));").classes("absolute inset-0"):
                pass
            
            # text 
            with ui.element("div").classes("relative text-center  drop-shadow-lg"):
                ui.label("Welcome to").classes("text-5xl font-lobster mb-4 typewriter")

                with ui.element("div").classes("flex flex-row justify-center font-Poppins font-bold gap-2 mb-6"):
                    ui.label("Garden").classes("text-8xl text-white")
                    ui.label("Fresh").classes("text-8xl text-orange-500")

                ui.button(icon="arrow_forward", text="Order Now").props("dense flat no-caps").classes(
                    "bg-white hover:bg-green-200 text-orange font-Poppins text-right px-6 py-3 mr-3 rounded-lg" 
                )
                # ui.button("View Menu").props("dense flat no-caps").classes(
                #     "bg-white hover:bg-orange-400 text-black font-Poppins px-6 py-3 rounded-full"
                # )

