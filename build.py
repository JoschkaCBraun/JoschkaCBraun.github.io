from typing import List, Dict, Tuple
from pybtex.database.input import bibtex


def get_personal_data() -> Tuple[List[str], str, str, str]:
    """Get personal data for the homepage."""
    name = ["Joschka", "Braun"]
    email = "joschkacbraun@gmail.com"
    twitter = "BraunJoschka"
    github = "JoschkaCBraun"
    linkedin = "joschka-braun"
    bluesky = "joschkabraun.bsky.social"
    orcid = "0009-0001-0281-2091"
    bio_text = f"""
                <p>I am a Machine Learning MSc student at the <a href="https://uni-tuebingen.de/" target="_blank">University of Tübingen</a>, working in the <a href="https://health-nlp.com/" target="_blank">Health-NLP</a> group Tübingen.</p>
                <p>
                    <span style="font-weight: bold;">Interests:</span> 
                    I am interested in the intersection of Deep Learning and Natural Language Processing to develop AI systems that are capable, trustworthy, and socially beneficial.
                    As AI technologies advance, I want to contribute to addressing the societal risks and ensure equitable benefits by improving scientific understanding and effective governance approaches.                   
                    </p>

                <p>
                    <span style="font-weight: bold;">Bio:</span>
                    I graduated with distinction in Computer Science from the <a href="https://uni-tuebingen.de/" target="_blank">University of Tübingen</a> in 2022, ranking in the top 5% of my class.
                    During my studies, I worked as a machine learning engineer at <a href="https://rawlab.de/" target="_blank">RAWLAB</a>, a startup specializing in engineering data processing, where I applied machine learning models to time-series analysis.
                    I am currently writing my Master's thesis on representation engineering in Large Language Models, supervised by <a href="https://scholar.google.ch/citations?user=UkzwC_EAAAAJ&hl=en" target="_blank">Seyed Ali Bahrainian</a> and 
                    <a href="https://scholar.google.com/citations?user=QQi1_rAAAAAJ&hl=en" target="_blank">Carsten Eickhoff</a> from the <a href="https://health-nlp.com/" target="_blank">Health-NLP</a> group at the University of Tübingen, and 
                    <a href="https://krasheninnikov.github.io/about/" target="_blank">Dmitrii Krasheninnikov</a> and 
                    <a href="https://scholar.google.ca/citations?user=5Uz70IoAAAAJ&hl=en" target="_blank">David Krueger</a> from the <a href="https://www.kasl.ai/" target="_blank">Krueger AI Safety Lab</a> at the University of Cambridge.
                </p>
                <p>Feel free to reach out to me via mail!</p>
                """
    footer = """
            <div class="col-sm-12" style="">
                <h4>Homepage Template</h4>
                <p>
                    This website is based on the template of <a href="https://m-niemeyer.github.io/" target="_blank">Michael Niemeyer</a>. Check out his <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">Github repository</a> for instructions on how to use it.
                </p>
            </div>
    """
    links_html = f"""
    <div class='container'>
        <div class='row justify-content-center'>
            <div class='col-auto mb-2'><a href='https://joschkacbraun.github.io/assets/pdf/CV_Joschka_Braun.pdf' target='_blank'><i class='fa fa-address-card fa-lg'></i> CV</a></div>
            <div class='col-auto mb-2'><a href='mailto:{email}'><i class='far fa-envelope-open fa-lg'></i> Mail</a></div>
            <div class='col-auto mb-2'><a href='https://github.com/{github}' target='_blank'><i class='fab fa-github fa-lg'></i> Github</a></div>
            <div class='col-auto mb-2'><a href='https://scholar.google.com/citations?&hl=en&user=hsNmAWYAAAAJ&hl=en' target='_blank'><i class='fa-solid fa-book'></i> Scholar</a></div>
            <div class='col-auto mb-2'><a href='https://orcid.org/{orcid}' target='_blank'><i class='fa-brands fa-orcid'></i> ORCID</a></div>
            <div class='col-auto mb-2'><a href='https://x.com/{twitter}' target='_blank'><i class='fab fa-x-twitter fa-lg'></i> X</a></div>
            <div class='col-auto mb-2'><a href='https://bsky.app/profile/{bluesky}' target='_blank'><i class="fa-brands fa-bluesky"></i> Bluesky</a></div>
            <div class='col-auto mb-2'><a href='https://www.linkedin.com/in/{linkedin}' target='_blank'><i class='fab fa-linkedin fa-lg'></i> LinkedIn</a></div>
        </div>
    </div>
    """

    return name, bio_text, footer, links_html


def get_author_dict() -> Dict[str, str]:
    """Get a dictionary of authors and their links."""
    return {
        "David Krueger": "https://scholar.google.ca/citations?user=5Uz70IoAAAAJ&hl=en",
        "Dmitrii Krasheninnikov": "https://krasheninnikov.github.io/about/",
        "Seyed Ali Bahrainian": "https://scholar.google.ch/citations?user=UkzwC_EAAAAJ&hl=en",
        "Carsten Eickhoff": "https://scholar.google.com/citations?user=QQi1_rAAAAAJ&hl=en",
        "NLP-health": "https://health-nlp.com/",
        "KASL": "https://www.kasl.ai/",
        "Usman Anwar" : "https://uzman-anwar.github.io/",
        "Robert Kirk" : "https://robertkirk.github.io/",
        "Daniel Tan" : "https://dtch1997.github.io/",
        "Bálint Mucsányi": "https://scholar.google.com/citations?user=NexA8EEAAAAJ&hl=en",
    }

def generate_person_html(
    persons,
    connection=", ",
    make_bold=True,
    make_bold_name="Joschka Braun",
    add_links=True,
) -> str:
    """Generate HTML for a list of persons."""
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in (
            p.get_part("first") + p.get_part("middle") + p.get_part("last")
        ):
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = (
                f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
            )
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s


def get_paper_entry(entry_key, entry) -> str:
    """Generate HTML for a paper entry."""
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    fields_key = "pdf" if "html" not in entry.fields.keys() else "html"

    if "award" in entry.fields.keys():
        s += f"""<a href="{entry.fields[fields_key]}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields[fields_key]}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {
        "html": "Project Page",
        "pdf": "Paper",
        "supp": "Supplemental",
        "video": "Video",
        "poster": "Poster",
        "code": "Code",
        "slides": "Slides",
    }
    i = 0
    for k, v in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += " / "
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f"[{entry_key}] Warning: Field {k} missing!")

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += (
        "\tauthor = {"
        + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}"
        + "}, \n"
    )
    for entr in ["title", "booktitle", "year"]:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += (
        " /"
        + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    )
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry) -> str:
    """Generate HTML for a talk entry."""
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html() -> str:
    """Generate HTML for the publications."""
    parser = bibtex.Parser()
    bib_data = parser.parse_file("publication_list.bib")
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html() -> str:
    """Generate HTML for the talks."""
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_projects_html() -> str:
    """Generate HTML for the projects."""
    parser = bibtex.Parser()
    bib_data = parser.parse_file("projects_list.bib")
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_paper_entry(k, bib_data.entries[k])
    return s

def get_misc_html() -> str:
    """Generate HTML for the miscellaneous."""
    parser = bibtex.Parser()
    bib_data = parser.parse_file("miscellaneous_list.bib")
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_paper_entry(k, bib_data.entries[k])
    return s

def get_index_html() -> str:
    """Generate the HTML for the index page."""
    pub = get_publications_html()
    talks = get_talks_html()
    projects = get_projects_html()
    misc = get_misc_html()
    name, bio_text, footer, links_html = get_personal_data()
    s = f"""
    <!doctype html>
    <html lang="en">
    <head>
        <!-- Existing meta tags and Bootstrap CSS link -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" crossorigin="anonymous">
        <link rel="stylesheet" <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" integrity="sha512-DTOQO9RWCH3ppGqcWaEA1BIZOC6xxalwEsw9c2QQeAIftl+Vegovlnee1c9QX4TctnWMn13TZye+giMm8e2LwA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
        </style>
        <title>{name[0] + ' ' + name[1]}</title>
        <link rel="icon" type="image/x-icon" href="assets/icon.ico">
    </head>

    <body>
        <div class="container">
            <div class="row" style="margin-top: 3em;">
                <div class="col-sm-12" style="margin-bottom: 1em; text-align: center;">
                    <h3 class="display-4"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
                    {links_html}
                </div>
                <div class="col-md-7">
                    {bio_text}
                </div>
                <div class="col-md-4 text-center" style="">
                    <img src="assets/img/profile.png" style="width: 100%; max-width: 280px; height: auto; border-radius: 50%;" alt="Profile picture">
                </div>
            </div>
            <div class="row" style="margin-top: 1em;">
                <div class="col-sm-12" style="">
                    <h4>Publications</h4>
                    {pub}
                </div>
            </div>
            <div class="row" style="margin-top: 3em;">
                <div class="col-sm-12" style="">
                    <h4>Talks</h4>
                    {talks}
                </div>
            </div>
            <div class="row" style="margin-top: 3em;">
                <div class="col-sm-12" style="">
                    <h4>Projects</h4>
                    {projects}
                </div>
            </div>
            <div class="row" style="margin-top: 3em;">
                <div class="col-sm-12" style="">
                    <h4>Miscellaneous</h4>
                    {misc}
                </div>
            </div>
            <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
                {footer}
            </div>
        </div>

        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
    </body>

    </html>
    """
    return s


def write_index_html(filename="index.html") -> None:
    s = get_index_html()
    with open(filename, "w") as f:
        f.write(s)
    print(f"Written index content to {filename}.")


if __name__ == "__main__":
    write_index_html("index.html")
