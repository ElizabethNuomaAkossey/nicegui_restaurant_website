from nicegui import ui

def render():
    with ui.element("div").classes("w-screen h-screen flex flex-row bg-grey-500"):
        # LEFT SECTION
        with ui.element("div").classes("w-[50%] h-screen flex flex-col justify-center items-center text-center p-6"):
            ui.label("Ghanaian Restaurant").classes("font-lobster text-2xl text-orange-500")
            ui.label("AKWAABA").classes("text-6xl font-bold font-Poppins text-black-300 mt-2")
            ui.html(
                "Experience the rich taste of Ghana with every bite,<br>"
                "fresh ingredients, traditional recipes,<br>"
                "and flavors that feel like home."
            ).classes("mt-6 text-m  font-Poppins")
            ui.link("OUR STORY").classes(
                "no-underline mt-5 px-6 py-3 rounded-lg text-black hover:text-orange-500"
            )

        # RIGHT SECTION
        with ui.element("div").classes("w-[50%] h-full flex items-center justify-center overflow-hidden"):
            ui.image("https://cdn.pixabay.com/photo/2022/04/20/14/39/burger-7145332_1280.png").classes(
        "w-[70%] h-[65%] object-cover rounded-xl transition-transform duration-500 ease-in transform hover:scale-110"
    )


                    