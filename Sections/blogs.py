from nicegui import ui

def render():
    with ui.element("section").classes("w-full py-16 bg-white"):
        # headings
        with ui.element("div").classes("text-center mb-12"):
            ui.label("Latest News").classes(
                "font-lobster italic text-orange-500 text-2xl"
            )
            ui.label("THE BLOG").classes(
                "text-4xl font-bold text-black mt-2"
            )

        # blog cards container
        with ui.row().classes("justify-center gap-8 flex-wrap px-6"):
            blogs = [
                {
                    "image": "https://cdn.pixabay.com/photo/2017/10/26/17/53/wine-2891894_1280.jpg",
                    "date": "21 Dec 2017",
                    "title": "Best Places For Wine",
                    "desc": "Phasellus lorem enim, luctus ut velit eget, convallis egestas eros."
                },
                {
                    "image": "https://cdn.pixabay.com/photo/2017/09/28/18/13/bread-2796393_1280.jpg",
                    "date": "15 Dec 2017",
                    "title": "Eggs And Cheese",
                    "desc": "Duis elementum, risus sit amet lobortis nunc justo condimentum ligula, vitae feugiat."
                },
                {
                    "image": "https://media.istockphoto.com/id/1124264599/photo/table-setting-for-an-event-party-or-wedding-reception.jpg?s=612x612&w=0&k=20&c=tp1x1duwJTUvesTEH4RrI0RZJkZ0Hv382y1zq__Y61M=",
                    "date": "12 Dec 2017",
                    "title": "Style The Wedding Party",
                    "desc": "Sed ornare ligula eget tortor tempor, quis porta tellus dictum."
                },
            ]

            for blog in blogs:
                with ui.element("div").classes(
                    "w-[320px] bg-white rounded-lg overflow-hidden flex flex-col"
                ):
                    # image with date
                    with ui.element("div").classes("relative w-full h-[200px] overflow-hidden"):
                        ui.image(blog["image"]).classes("w-full h-full object-cover")
                        ui.label(blog["date"]).classes(
                            "absolute bottom-2 left-2 bg-black/60 text-white text-xs px-2 py-1 rounded"
                        )

                    # content
                    with ui.element("div").classes("p-4 flex flex-col flex-1"):
                        ui.label(blog["title"]).classes(
                            "text-lg font-bold text-gray-900 mb-2 uppercase"
                        )
                        ui.label(blog["desc"]).classes(
                            "text-sm text-gray-600 mb-4"
                        )
                        ui.link("Continue Reading →", "#").classes(
                            "mt-auto text-xs tracking-widest uppercase text-gray-700 hover:text-orange-500 no-underline"
                        )
