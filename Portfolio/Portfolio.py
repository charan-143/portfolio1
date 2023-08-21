"""Welcome to Reflex! This file outlines the steps to create a basic app."""


import reflex as rx
from rxconfig import config


def menu() -> rx.Component:
    return rx.hstack(
        rx.text("about_me", font_size=20, color="#e28743"),
        rx.spacer(),
        rx.spacer(),
        rx.text("education", font_size=20, color="#e28743"),
        rx.spacer(),
        rx.spacer(),
        rx.text("work_experience", font_size=20, color="#e28743"),
        rx.spacer(),
        rx.spacer(),
        rx.text("interests", font_size=20, color="#e28743"),
        rx.spacer(),
        rx.spacer(),
        rx.text("projects", font_size=20, color="#e28743"),
        rx.spacer(),
        rx.spacer(),
        rx.text("skills", font_size=20, color="#e28743"),
        rx.spacer(),
        rx.spacer(),
        rx.text("blogs", font_size=20, color="#e28743"),
        rx.spacer(),
        rx.spacer(),
        rx.text("certificates", font_size=20, color="#e28743"),

        padding_y="1em",

    )


def about_me() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text("Devanapally Charan Tej", font_size=40,
                    float="left", color="#e28743"),
            rx.text(
                """Hi, I'm Devanapally Charan Tej, a passionate Python developer and blogger at Hashnode.
                             With hands-on experience in machine learning and data analytics,
                             I have collaborated with renowned researchers at IIIT Bangalore.
                              My expertise lies in building AI-powered projects like the Jarvis Virtual
                               Assistant and the Currency Converter Conversational Chatbot. """,
                float="left", font_size=20, width=600, color="#2596be",
            ),
            rx.hstack(
                rx.image(src="/linkedin.jpg", height="40px", ),
                rx.link(

                    rx.text("devanapallycharantej", font_size=15),
                    href="https://www.linkedin.com/in/devanapallycharantej/",
                    is_external=True, color="#be4d25"

                ),
                rx.spacer(),
                rx.spacer(),

                rx.image(src="/github_logo.jpg", height="40px"),
                rx.link(
                    rx.text("charan-143", font_size=15),
                    href="https://github.com/charan-143",
                    is_external=True, color="#be4d25"
                ),
                height="80px",

            ),

            width=750

        ),
        rx.vstack(
            rx.image(
                src="/profile.jpg", height=250, float="right",
                border_radius="15px 15px",
                border="5px solid #555",
                box_shadow="lg",
                border_color="#e28743"
            ),
            rx.text("ML/DL Enthusiast ", font_size=20, color="#be4d25")

        ),

        width=1000, padding_y="2em",

    )


def blogs() -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.vstack(
                rx.hstack(
                    rx.link(
                        rx.text("Create Your Own Jarvis: A Python-Based Virtual Assistant for PC",
                                as_="b",
                                font_size=30,
                                color="#e28743",
                                float="left"),
                        is_external=True,
                        href="https://charantej.hashnode.dev/create-your-own-jarvis-a-python-based-virtual-assistant-for-pc"
                    ),
                    rx.spacer(),
                    rx.spacer(),
                    rx.spacer(),
                    rx.spacer(),
                    rx.text("@hashnode", font_size=20,
                            float="left", color="#be4d25"),
                    rx.spacer(),
                    rx.spacer(),

                ),
                rx.stack(
                    rx.text(
                        """This is a blog about a virtual assistant project called Jarvis made via python.
                                     This blog is a beginner-friendly guide to making a project and exploring python libraries. 
                                     This blog contains the basic prerequisites of a virtual assistant""",
                        font_size=20,
                        color="#2596be",
                        width=700,
                    )
                ),
                rx.spacer(),
                rx.divider(border_color="#ded9d9", width=800),
                rx.spacer(),

                rx.hstack(
                    rx.link(
                        rx.text("Supercharge Your Jarvis: Add Exciting Features for Enhanced Functionality",
                                as_="b",
                                font_size=30,
                                color="#e28743",
                                float="left"),
                        is_external=True,
                        href="https://charantej.hashnode.dev/supercharge-your-jarvis-add-exciting-features-for-enhanced-functionality"
                    ),
                    rx.spacer(),
                    rx.spacer(),
                    rx.spacer(),
                    rx.spacer(),
                    rx.text("@hashnode", font_size=20,
                            float="left", color="#be4d25"),
                    rx.spacer(),
                    rx.spacer(),

                ),
                rx.stack(
                    rx.text(
                        """This is the continuation of the Jarvis Virtual Assistant Project for Beginners blog.
                                     As the title says this blog helps us to automate our PC with the help of Jarvis.""",
                        font_size=20,
                        color="#2596be",
                        width=700,
                    )
                ),

                rx.spacer(),
                rx.divider(border_color="#ded9d9", width=800),
                rx.spacer(),

                rx.hstack(
                    rx.link(
                        rx.text(
                            "Demystifying AI, ML, and DL: Unraveling the Intricacies of Modern Intelligence",
                            as_="b",
                            font_size=30,
                            color="#e28743",
                            float="left"),
                        is_external=True,
                        href="https://charantej.hashnode.dev/demystifying-ai-ml-and-dl-unraveling-the-intricacies-of-modern-intelligence"
                    ),
                    rx.spacer(),
                    rx.spacer(),
                    rx.spacer(),
                    rx.spacer(),
                    rx.text("@hashnode", font_size=20,
                            float="left", color="#be4d25"),
                    rx.spacer(),
                    rx.spacer(),

                ),
                rx.stack(
                    rx.text(
                        """This blog is around the difference between the most click bait buzz words AI, ML, DL.
                                     The blogs tells the history of the AI. 
                                    It also tells what is the difference between them.""",
                        font_size=20,
                        color="#2596be",
                        width=700,
                    )
                ),
                rx.spacer(),
                padding_y="1em",

            ),
            width=1000,
            border_radius="15px 15px",
            border="1px solid #555",
            box_shadow="lg",
            border_color="#ded9d9"

        ),

        padding_y="2em",

    )


def certificates() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.image(
                src="/data_analysis.jpg",
                height=300,
                border_radius="15px 15px",
                border="5px solid #555",
                box_shadow="lg",
            ),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.image(
                src="/data_visualization.jpg",
                height=300,
                border_radius="15px 15px",
                border="5px solid #555",
                box_shadow="lg",
            ),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.image(
                src="/data_science.jpg",
                height=300,
                border_radius="15px 15px",
                border="5px solid #555",
                box_shadow="lg",
            ),
            padding_y="2em",

        ),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),

        rx.vstack(
            rx.image(
                src="/digital_marketing.jpg",
                height=300,
                border_radius="15px 15px",
                border="5px solid #555",
                box_shadow="lg",
            ),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.image(
                src="/internship.jpg",
                height=300,
                border_radius="15px 15px",
                border="5px solid #555",
                box_shadow="lg",
            ),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.image(
                src="/sabrang.jpg",
                height=300,
                border_radius="15px 15px",
                border="5px solid #555",
                box_shadow="lg",
            ),
            padding_y="2em",

        )
    )


def education() -> rx.Component:
    return rx.hstack(

        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.text("JK Lakshmipat University",
                            font_size=40,
                            as_="b",
                            color="#e28743",
                            ),
                    rx.hstack(
                        rx.text('"BTech"', font_size=20, color="#2596be", ),
                        rx.spacer(),
                        rx.spacer(),
                        rx.spacer(),
                        rx.text('"Computer Science"',
                                font_size=20, color="#2596be", ),

                    ),
                    rx.hstack(
                        rx.text('"2020-24"', font_size=20, color="#be4d25"),
                        rx.spacer(),
                        rx.spacer(),
                        rx.spacer(),
                        rx.text('"6.631"', font_size=20, color="#be4d25"),

                    )
                ),

                height=250,
                width=330,
                border_radius="15px 15px",
                border="1px solid #555",
                box_shadow="lg",
                border_color="#ded9d9",
                padding_y="0.5em",

            )
        ),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        rx.vstack(

            rx.box(
                rx.vstack(
                    rx.text("Sri Gayatri Junior College",
                            font_size=40, as_="b", color="#e28743", ),
                    rx.hstack(
                        rx.text('"12th Pass"', font_size=20,
                                color="#2596be", ),
                        rx.spacer(),
                        rx.spacer(),
                        rx.spacer(),
                        rx.text('"PCM"', font_size=20, color="#2596be", ),

                    ),
                    rx.hstack(
                        rx.text('"2018-20"', font_size=20, color="#be4d25"),
                        rx.spacer(),
                        rx.spacer(),
                        rx.spacer(),
                        rx.text('"9.6"', font_size=20, color="#be4d25"),

                    )
                ),

                height=250,
                width=350,
                border_radius="15px 15px",
                border="1px solid #555",
                box_shadow="lg",
                border_color="#ded9d9",
                padding_y="0.5em",

            )

        ),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        rx.vstack(

            rx.box(
                rx.vstack(
                    rx.text("Millennium High School", font_size=40,
                            as_="b", color="#e28743", ),
                    rx.hstack(
                        rx.text('"Matriculation"', font_size=20,
                                color="#2596be", ),

                    ),
                    rx.hstack(
                        rx.text('"2018-19"', font_size=20, color="#be4d25"),
                        rx.spacer(),
                        rx.spacer(),
                        rx.spacer(),
                        rx.text('"7.8"', font_size=20, color="#be4d25"),

                    )
                ),

                height=250,
                width=350,
                border_radius="15px 15px",
                border="1px solid #555",
                box_shadow="lg",
                border_color="#ded9d9",
                padding_y="0.5em",

            )

        ),

        padding_y="2em",

    )


def interests() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.text("artificial_intelligence", font_size=20, color="#e28743"),
            rx.spacer(),
            rx.spacer(),
            rx.text("machine_learning", font_size=20, color="#e28743"),
            rx.spacer(),
            rx.spacer(),
            rx.text("deep_learning", font_size=20, color="#e28743"),
            rx.spacer(),
            rx.spacer(),
            rx.text("llm's", font_size=20, color="#e28743"),
            rx.spacer(),
            rx.spacer(),
            rx.text("computer_vision", font_size=20, color="#e28743"),
        ),

        padding_y="2em",

    )


def skills() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.hstack(
                rx.text("pytorch", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("tensorflow", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("opencv", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("flet", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("reflex", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("communication", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("sci-kit_learn", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("sql", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),

            ),
            rx.hstack(
                rx.text("pygame", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("problem_solving", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("data_analysis", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("data_visualization", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("data_science", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("keras", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),
                rx.text("dsa", font_size=20, color="#e28743"),
                rx.spacer(),
                rx.spacer(),

            )
        ),
        padding_y="2em",

    )


def projects() -> rx.Component:
    return rx.hstack(

        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.link(
                        rx.text('"Jarvis Virtual Assistant"', font_size=40,
                                as_="b",
                                color="#e28743", ),
                        href="https://github.com/charan-143/jarvis-project",
                        is_external=True,

                    ),
                    rx.hstack(
                        rx.text('"Feb,2022 "', font_size=20,
                                color="#2596be", ),

                    ),
                    rx.hstack(

                        rx.text('"This is a project for basic understanding on AI.'
                                ' This Jarvis projet is a virtual assistant which will do certain tasks which '
                                'are mentiond in the code like opening youtube, searching on wikipedia etc.."',
                                font_size=20, color="#be4d25"),

                    )
                ),

                height=300,
                width=650,
                border_radius="15px 15px",
                border="1px solid #555",
                box_shadow="lg",
                border_color="#ded9d9",
                padding_y="0.5em",

            ),

            rx.spacer(),
            rx.spacer(),
            rx.spacer(),

            rx.box(
                rx.vstack(
                    rx.link(
                        rx.text("Customer Segmentation", font_size=40,
                                as_="b", color="#e28743", ),
                        href="https://github.com/charan-143/ML-Projects/tree/main/Customer%20Segmentation%20ML%20Project",
                        is_external=True,
                    ),
                    rx.hstack(
                        rx.text('"Jun,2022 - Jun,2022"',
                                font_size=20, color="#2596be"),

                    ),
                    rx.hstack(
                        rx.text(
                            '"The customers dataset from Kaggle is divided into clusters by using a k-means clustering algorithm.'
                            ' This helped in analyzing the data"',
                            font_size=20,
                            color="#be4d25"
                        ),

                    )
                ),

                height=300,
                width=650,
                border_radius="15px 15px",
                border="1px solid #555",
                box_shadow="lg",
                border_color="#ded9d9",
                padding_y="0.5em",

            ),

        ),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        rx.vstack(

            rx.box(
                rx.vstack(
                    rx.link(
                        rx.text("Currency Converter Conversational Chatbot",
                                font_size=40, as_="b", color="#e28743", ),
                        href="https://github.com/charan-143/currencyconverterchatbot",
                        is_external=True,

                    ),
                    rx.hstack(
                        rx.text('"Jun,2022 - Jun,2022"',
                                font_size=20, color="#2596be"),

                    ),
                    rx.hstack(
                        rx.text('"This project is a telegram integrated chatbot (Telegram bot).'
                                ' The technology used in the chatbot is Dialogflow, Flask(Backend),'
                                ' and API(free.currconv.com). The chatbot is connected to the backend through a webhook."',
                                font_size=20,
                                color="#be4d25"
                                ),

                    )
                ),

                height=300,
                width=650,
                border_radius="15px 15px",
                border="1px solid #555",
                box_shadow="lg",
                border_color="#ded9d9",
                padding_y="0.5em",

            ),

            rx.spacer(),
            rx.spacer(),
            rx.spacer(),

            rx.box(
                rx.vstack(
                    rx.text("Med-e-Bot", font_size=40,
                            as_="b", color="#e28743", ),

                    rx.hstack(
                        rx.text('"Jun,2022 - Jun,2022"',
                                font_size=20, color="#2596be"),

                    ),
                    rx.hstack(
                        rx.text(
                            '"It is a robot that is made for doctors in the pandemic.'
                            'It supplies food and medicines for patients in hospitals and makes hospital staff interact '
                            'less with patients and be safe from getting infected up to some extent"',
                            font_size=20,
                            color="#be4d25"
                        ),

                    )
                ),

                height=300,
                width=650,
                border_radius="15px 15px",
                border="1px solid #555",
                box_shadow="lg",
                border_color="#ded9d9",
                padding_y="0.5em",

            ),

        ),
        padding_y="2em",

    )


def work_experience() -> rx.Component:
    return rx.hstack(

        rx.vstack(
            rx.box(
                rx.vstack(
                    rx.text("Summer Intern",
                            font_size=40,
                            as_="b",
                            color="#e28743",
                            ),
                    rx.hstack(
                        rx.text('"DIGIMONK Ltd."', font_size=20,
                                color="#2596be", ),
                        rx.spacer(),
                        rx.spacer(),
                        rx.spacer(),
                        rx.text('"Bishop Auckland, England"',
                                font_size=20, color="#2596be", ),
                        rx.spacer(),
                        rx.spacer(),
                        rx.spacer(),
                        rx.text('"May,2023 - July,2023"',
                                font_size=20, color="#2596be", ),

                    ),
                    rx.hstack(

                        rx.text('"Worked on a live project on Digital Activity Platform Development '
                                'which is developing Smart Gloves for the rehabilitation and recovery of patients."',
                                font_size=20, color="#be4d25"),

                    )
                ),

                height=300,
                width=650,
                border_radius="15px 15px",
                border="1px solid #555",
                box_shadow="lg",
                border_color="#ded9d9",
                padding_y="0.5em",

            )
        ),
        rx.spacer(),
        rx.spacer(),
        rx.spacer(),
        rx.vstack(

            rx.box(
                rx.vstack(
                    rx.text("Research Intern", font_size=40,
                            as_="b", color="#e28743", ),
                    rx.hstack(
                        rx.text('"Dr. Amit Chattopadhyay"',
                                font_size=20, color="#2596be", ),
                        rx.spacer(),
                        rx.spacer(),
                        rx.spacer(),
                        rx.text('"bangalore"', font_size=20,
                                color="#2596be", ),
                        rx.spacer(),
                        rx.spacer(),
                        rx.spacer(),
                        rx.text('"June,2022 - August,2022"',
                                font_size=20, color="#2596be"),

                    ),
                    rx.hstack(
                        rx.text(
                            '"I helped Prof. Amit Chattopadhyay(IIIT Banglore) with his research project on the title'
                            ' of Geometric and Topological methods on Machine'
                            ' learning using a clustering Machine learning algorithm."',
                            font_size=20,
                            color="#be4d25"
                        ),

                    )
                ),

                height=300,
                width=650,
                border_radius="15px 15px",
                border="1px solid #555",
                box_shadow="lg",
                border_color="#ded9d9",
                padding_y="0.5em",

            )

        ),

        padding_y="2em",

    )


def invalid_keyword() -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.text("Please type ? to know which words to search.",
                    font_size=20, color="#e28743")
        ),
        padding_y="1em",

    )


def search_form(InputState) -> rx.Component:
    return (rx.box(
        rx.input_group(
            rx.input_left_element(
                rx.text("$ ", font_size=30, height="0.8em", color="#e28743")
            )
        ),

        rx.input(

            width=600,
            height=65,
            font_size=25,
            on_change=InputState.set_input_value,
            padding_left="1.2em",
            border_color="#abdbe3",
            placeholder="Hint: type ? to know more...",
            focus_border_color="#e28743",
            is_required=False,
            type_="text",
            value=InputState.input_value,
            id="command"

        ),
        # rx.button("Run",width=70, height=65, font_size=30,left=5,bottom=1),
        rx.button(rx.image(src="/play.svg"),
                  width=70,
                  height=65,
                  left=5,
                  bottom=1,
                  opacity=50,
                  color_scheme="whatsapp",
                  on_click=lambda: InputState.get_book_by_title()

                  ),
    ))


def return_page(command: str) -> rx.Component:
    if command == "about_me" or command == "about me" or command == "aboutme":
        return about_me()

    elif command == "?":
        return menu()

    elif command == "blogs":
        return blogs()

    elif command == "interests":
        return interests()

    elif command == "skills":
        return skills()

    elif command == "work_experience" or command == "work experience" or command == "work" or command == "experience" or command == "workexperience":
        return work_experience()

    elif command == "projects":
        return projects()

    elif command == "certificates":
        return certificates()

    elif command == "education":
        return education()

    else:
        return invalid_keyword()


class InputState(rx.State):
    input_value: str = ""

    def set_input_value(self, input_value: str):
        """Handle the form submit."""
        self.input_value = input_value

    def get_book_by_title(self):
        get_page(self.input_value)

        app.compile()

        if self.input_value is None:
            # return rx.redirect(f"https://charantej.vercel.app:3000/")
            return rx.redirect(f"https://localhost:3000/")

        if self.input_value == "?":
            route = "menu"
        else:
            route = self.input_value.replace(" ", "-").replace("_", "-")
        # return rx.redirect(f"https://charantej.vercel.app:3000/{route.lower()}")
        return rx.redirect(f"https://localhost:3000/{route.lower()}")


def book_ui(command):
    if command is None:
        return rx.center(
            rx.vstack(
                rx.box(
                    rx.text(InputState.input_value, color_scheme="green"),
                ),
                rx.hstack(
                    search_form(InputState, ),
                ),
            ),
            padding_y="9em",
            font_size="2em",
            text_align="center",
        )
    else:
        return rx.center(
            rx.vstack(
                rx.box(
                    rx.text(InputState.input_value, color_scheme="green"),
                ),
                rx.hstack(
                    search_form(InputState, ),
                ),

                return_page(command)

            ),
            padding_y="9em",
            font_size="2em",
            text_align="center",
        )


def get_page(command: str):
    def return_layout() -> rx.Component:
        return book_ui(command)

    if command == "?":
        route = "menu"
    else:
        route = command.replace(" ", "-").replace("_", "-")

    @rx.page(route=f"/{route.lower()}", title=command)
    def command_page_route() -> rx.Component:
        return return_layout()

    return command_page_route


@rx.page(route="/", title="search")
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.box(
                rx.text(InputState.input_value, color="#ff4d4d"),
            ),
            rx.hstack(
                search_form(InputState),
            ),
            # rx.text(InputState.form_data.to_string()),

        ),
        padding_y="9em",
        font_size="2em",
        text_align="center",
    )


# Add state and page to the app.
app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    ],
    assets="../assets/",

)

app.compile()
