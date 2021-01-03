import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WebXplore",
    version="1.0.3",
    author="Arnav Nidumolu",
    author_email="arnav.nidumolu@gmail.com",
    description="Explore Web Pages - Scrapers and Crawlers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arnavn101/WebXplore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
    ],
    keywords=" ".join(
        ["web", "crawling", "scraping", "nlp"]
    ),
    install_requires=["nltk", "requests", "beautifulsoup4", "google", "numpy", "pandas", "textblob",
                      "sklearn", "newsapi-python", "praw", "tweepy", "readability-lxml"],
    python_requires=">=3.7",
)
