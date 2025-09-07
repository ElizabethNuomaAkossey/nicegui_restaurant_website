from nicegui import ui

def render():
    with ui.element("div").classes("w-screen h-screen flex flex-row"):
        # LEFT SECTION
        with ui.element("div").classes("w-[50%] h-screen flex flex-col justify-center items-center text-center p-6"):
            ui.label("Ghanaian Restaurant").classes("font-lobster text-xl text-orange-500")
            ui.label("AKWAABA").classes("text-5xl font-bold font-Poppins text-black-300 mt-2")
            ui.html(
                "Experience the rich taste of Ghana with every bite,<br>"
                "fresh ingredients, traditional recipes,<br>"
                "and flavors that feel like home."
            ).classes("mt-6 text-m  font-Poppins")
            ui.link("OUR STORY").classes(
                "no-underline mt-5 px-6 py-3 rounded-lg text-black hover:text-orange-500"
            )

        # RIGHT SECTION
        with ui.element("div").classes("w-[50%] h-full items-center justify-center"):
            ui.image("https://weeatatlast.com/wp-content/uploads/2022/11/jollof-rice-with-chicken.jpg").classes(
                "w-[70%] h-[70%] object-cover m-20 rounded-xl"
            )

                    