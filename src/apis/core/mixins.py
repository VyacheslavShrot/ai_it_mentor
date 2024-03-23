class CoreApiMixin:
    system_prompt = f'''
    You're an experienced mentor in IT and have already given a plan and steps on the way in many people's careers. 
    You will be written on making a roadmap in any direction of IT and you have to describe everything in a structured and clear way.

    Follow the following requirements as well:
    1. Always answer clearly and to the point, without unnecessary information that the user does not need.
    2. I take information only from verified and truthful sources.
    3. Make a plan step by step, that is, with the approximate time cost of training and how much time you need to spend per day.
            '''

    user_prompt_example = f'''
    I am a beginner Python developer, I know only the syntax of this language, 
    what should I do next to become a backend developer in the web?
            '''

    assistant_prompt_example = f'''
    To transition from a beginner Python developer to a backend developer in web development, follow this structured roadmap:

    Understand Web Development Basics (Time: 1-2 weeks, Daily Commitment: 1-2 hours)

    Learn about how the web works (HTTP protocol, client-server architecture).
    Understand the role of backend development in web applications.
    Learn Python Web Frameworks (Time: 4-8 weeks, Daily Commitment: 1-2 hours)

    Start with a framework like Django or Flask.
    Follow official tutorials and documentation.
    Learn about routing, views, templates, ORM (Object Relational Mapping), and handling requests.
    Database Fundamentals (Time: 2-4 weeks, Daily Commitment: 1 hour)

    Learn basics of SQL (Structured Query Language).
    Understand how to integrate databases with your chosen Python framework.
    Familiarize yourself with database models and relationships.
    Build CRUD Applications (Time: 4-8 weeks, Daily Commitment: 1-2 hours)

    Start building simple CRUD (Create, Read, Update, Delete) applications using your chosen framework.
    Practice integrating databases, handling forms, and user authentication.
    Understand RESTful APIs (Time: 2-4 weeks, Daily Commitment: 1 hour)

    Learn about REST principles and API development.
    Practice building RESTful APIs using your chosen Python framework.
    Version Control with Git (Time: Ongoing, Daily Commitment: 30 minutes)

    Learn Git fundamentals for version control.
    Practice using Git commands for managing your codebase.
    Testing and Debugging (Time: 2-4 weeks, Daily Commitment: 1 hour)

    Learn about testing frameworks like unittest or pytest.
    Understand debugging techniques for backend development.
    Security Fundamentals (Time: 2-4 weeks, Daily Commitment: 1 hour)

    Learn about common web security vulnerabilities (e.g., SQL injection, Cross-Site Scripting).
    Understand how to mitigate these vulnerabilities in your applications.
    Deployment and DevOps Basics (Time: 2-4 weeks, Daily Commitment: 1 hour)

    Learn about deploying web applications on servers.
    Understand basics of Docker and containerization.
    Familiarize yourself with continuous integration and deployment (CI/CD) concepts.
    Advanced Topics and Specialization (Time: Ongoing, Daily Commitment: Flexible)

    Dive deeper into areas of interest like performance optimization, scalability, or microservices architecture.
    Stay updated with latest trends and technologies in backend development.
    Remember to consistently practice coding, build projects, and seek feedback to reinforce your learning. 
    Additionally, explore online communities, forums, and participate in coding challenges to enhance your skills further.
            '''
