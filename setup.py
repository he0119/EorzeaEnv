import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="EorzeaEnv",
    version="1.0.0",
    author="Elton H.Y. Chou",
    author_email="plscd748@gmail.com",
    license="MIT",
    description="Final Fantasy XIV weather & time tools.",
    keywords='eorzea ffxiv ff14',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EltonChou/EorzeaEnv",
    packages=setuptools.find_packages(),
    install_requires=['numpy'],
    python_requires='>=3.6.0',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Bug Reports': 'https://github.com/EltonChou/EorzeaEnv/issues',
        'Thanks!': 'https://github.com/Rogueadyn/SaintCoinach',
        'Source': 'https://github.com/EltonChou/EorzeaEnv',
    },
)
