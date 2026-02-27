from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    skills = {
        "C++": 85,
        "Python": 90,
        "C": 75,
        "Java": 70,
        "JavaScript": 70,
        "HTML": 85,
        "CSS": 80,
        "MySQL": 75,
        "Power BI": 70,
        "Excel": 85
    }

    projects = [
        {
            "title": "Crossword Filler AI Tool",
            "description": "Developed an AI-based crossword solver using backtracking, pattern matching, and constraint-based search algorithms to efficiently generate valid word placements.",
            "tech": "C++, HTML, CSS",
            "github": "https://github.com/priyaagrawal2/Crossword_filler"
        },
        {
            "title": "Myntra Sales Dashboard",
            "description": "Designed an interactive Excel dashboard using pivot tables, slicers, Power Query, and dynamic visualizations to analyze large-scale sales data and generate KPIs.",
            "tech": "Excel, Power Query, Python",
            "github": "https://github.com/priyaagrawal2/Myntra_Dashboard"
        },
        {
            "title": "Gardening Chatbot (Patent Filed)",
            "description": "Built a conversational AI chatbot providing crop recommendations, planting timelines, and nutrient guidance using Gemini API with backend data pipelines.",
            "tech": "Python, AI, Gemini API, CSS, JavaScript",
            "github": "https://github.com/priyaagrawal2/Gardening_Chatbot.github.io"
        }
    ]

    education = [
        {
            "degree": "B.Tech - Computer Science and Engineering",
            "institution": "Lovely Professional University, Punjab",
            "score": "CGPA: 7.32"
        },
        {
            "degree": "Intermediate",
            "institution": "Baba Mungipa Vidya Peeth Sr. Sec. School",
            "score": "79%"
        },
        {
            "degree": "Matriculation",
            "institution": "Baba Mungipa Vidya Peeth Sr. Sec. School",
            "score": "92%"
        }
    ]

    achievements = [
        "Filed Patent: Gardening Chatbot (2025)"
    ]

    training = [
        "Placement Programming Essentials with C++, DSA & Python - Board Infinity"
    ]

    certificates = [
        "Build Generative AI Apps and Solutions with No-Code Tools",
        "Computational Theory: Language Principle & Finite Automata Theory",
        "NPTEL: Cloud Computing"
    ]

    return render_template(
        "index.html",
        skills=skills,
        projects=projects,
        education=education,
        achievements=achievements,
        training=training,
        certificates=certificates
    )

if __name__ == "__main__":
    app.run(debug=True)