# Stage 1: Build
FROM node:20 AS build

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the source code
COPY . .

# Build the React app
RUN npx react-scripts build



RUN chmod +x ./node_modules/.bin/react-scripts


# Stage 2: Serve with Nginx
FROM nginx:stable-alpine

# Copy the build output to Nginx's html folder
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 3000
EXPOSE 3000

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
