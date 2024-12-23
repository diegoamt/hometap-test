# Hometap code challenge

## Backend

I used FastAPI because it requires a minimal setup to start bilding a REST API, the opposite case of Django rest-framework. Also because FastAPI is asynchronous by default and in this case it was useful to optimize the two external HTTP requests using asyncio.

see documentation [here](backend/README.md)

## Frontend

I used React (using Vite to create the project). I didn't use Angular because of its complexity in comparison with React. Vue also was a good choice, but I prefer to use React because it has more documentation and a larger community support. I also added Typescript to make it more robust and Tailwind CSS for the CSS because it's faster adding styles to the components by reusing existing Tailwind classes.

see documentation [here](frontend/README.md)