from typing import List, Dict, Tuple
from pybtex.database.input import bibtex
# ignore f strings linter error (f string without interpolation W1309)
# pylint: disable=W1309

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
                <p>
                    I am a machine learning researcher focused on developing trustworthy, interpretable, and socially beneficial AI systems.
                </p>
                <p>
                    Currently, I'm a scholar in the <a href="https://www.matsprogram.org/" target="_blank">ML Alignment & Theory Scholars (MATS) Program</a>, working on Scalable Oversight and AI Control with 
                    <a href="https://scholar.google.com/citations?user=p_aH5fgAAAAJ&hl=en" target="_blank">David Lindner</a>, 
                    <a href="https://rzimmermann.com/" target="_blank">Roland Zimmermann</a>, and 
                    <a href="https://scholar.google.com/citations?user=LoT0z6oAAAAJ&hl=en" target="_blank">Scott Emmons</a>.
                </p>
                <p>
                    My previous research includes work on the reliability of steering vectors in Large Language Models with <a href="https://krasheninnikov.github.io/about/" target="_blank">Dmitrii Krasheninnikov</a> and <a href="https://scholar.google.ca/citations?user=5Uz70IoAAAAJ&hl=en" target="_blank">David Krueger</a> at the <a href="https://www.kasl.ai/" target="_blank">Krueger AI Safety Lab</a> at the University of Cambridge. I have also worked on applications of representation engineering at the <a href="https://health-nlp.com/" target="_blank">Health-NLP</a> group, supervised by 
                    <a href="https://scholar.google.ch/citations?user=UkzwC_EAAAAJ&hl=en" target="_blank">Seyed Ali Bahrainian</a> and 
                    <a href="https://scholar.google.com/citations?user=QQi1_rAAAAAJ&hl=en" target="_blank">Carsten Eickhoff</a>.
                </p>
                <p>
                    I am passionate about public debate and democratic discourse to shape informed perspectives and drive effective policy.
                </p>
                <p>
                    I hold a Master’s degree in Machine Learning and a Bachelor’s degree in Computer Science from the <a href="https://uni-tuebingen.de/" target="_blank">University of Tübingen</a>. My research sits at the intersection of Deep Learning and Natural Language Processing, motivated by the challenge of building safe and equitable AI systems. As AI technologies improve, I aim to help address societal risks and promote equitable benefits by advancing scientific understanding and supporting effective governance.
                </p>
                <p>
                    Feel free to reach out to me via mail!
                </p>
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
            <div class='col-auto mb-2'><a href='https://huggingface.co/Joschka' target='_blank'><img src='assets/huggingface-logo.svg' alt='Hugging Face' style='width: 27px; height: 27px; vertical-align: middle; margin-right: 4px;'> Hugging Face</a></div>
            <div class='col-auto mb-2'><a href='https://scholar.google.com/citations?&hl=en&user=hsNmAWYAAAAJ&hl=en' target='_blank'><i class='fa-solid fa-book'></i> Scholar</a></div>
            <div class='col-auto mb-2'><a href='https://orcid.org/{orcid}' target='_blank'><i class='fa-brands fa-orcid'></i> ORCID</a></div>
            <div class='col-auto mb-2'><a href='https://x.com/{twitter}' target='_blank'><i class='fab fa-x-twitter fa-lg'></i> X</a></div>
            <div class='col-auto mb-2'><a href='https://bsky.app/profile/{bluesky}' target='_blank'><img src='assets/bluesky-logo.svg' alt='Bluesky' style='width: 16px; height: 16px; vertical-align: middle; margin-right: 4px; display: inline-block;' onerror="this.style.display='none'; this.nextSibling.style.display='inline';"><i class='fas fa-cloud' style='display: none; color: #0085FF;'></i> Bluesky</a></div>
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
        "Damon Falck": "https://scholar.google.com/citations?hl=en&user=_TQEoLgAAAAJ",
        "Yeonwoo Jang": "https://scholar.google.com/citations?user=jXfklAEAAAAJ",
        "Roland S. Zimmermann": "https://rzimmermann.com/",
        "Scott Emmons": "https://scholar.google.com/citations?user=LoT0z6oAAAAJ&hl=en",
        "David Lindner": "https://scholar.google.com/citations?user=p_aH5fgAAAAJ&hl=en",
    }


def generate_person_html(
    persons,
    connection=", ",
    make_bold=True,
    make_bold_name="Joschka Braun",
    add_links=True,
) -> str:
    """Generate HTML for a list of persons. Preserves literal asterisks in names but matches links/bold against a canonical name without asterisks."""
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

        # Keep the original display (which may include trailing asterisks)
        display_name = string_part_i
        # Canonical name for matching (strip any asterisks and surrounding whitespace)
        canonical_name = display_name.replace("*", "").strip()

        # Determine formatting
        is_bold = make_bold and canonical_name == make_bold_name
        is_link = add_links and (canonical_name in links.keys())

        rendered = display_name
        if is_bold:
            rendered = f'<span style="font-weight: bold">{rendered}</span>'
        if is_link:
            href = links[canonical_name]
            # Make the whole rendered text clickable
            rendered = f'<a href="{href}" target="_blank">{rendered}</a>'

        if p != persons[-1]:
            rendered += connection
        s += rendered
    return s


def get_paper_entry(entry_key, entry) -> str:
    """Generate HTML for a paper entry."""
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    # Prioritize slides over html for title link
    if "pdf" in entry.fields.keys():
        fields_key = "pdf"
    elif "slides" in entry.fields.keys():
        fields_key = "slides"
    else:
        fields_key = "html"

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
        "arxiv": "arXiv",
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
    
    # Add eprint field if it exists
    if "eprint" in entry.fields.keys():
        cite += f"\teprint = " + "{" + f"{entry.fields['eprint']}" + "}, \n"
    
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

def get_public_debate_entry(entry_key, entry) -> str:
    """Generate HTML for a public debate entry."""
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Debate image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['description']}</span><br>"""

    artefacts = {'video': 'Video', 'link': 'Link'}
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

def get_public_debates_html() -> str:
    """Generate HTML for the public debates."""
    parser = bibtex.Parser()
    bib_data = parser.parse_file('public_debates_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_public_debate_entry(k, bib_data.entries[k])
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
    public_debates = get_public_debates_html()
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
                    <h4>Public Debates</h4>
                    {public_debates}
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
