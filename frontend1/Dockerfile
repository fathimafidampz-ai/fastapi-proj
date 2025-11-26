# Stage 1: Build React app
FROM node:20 AS build

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the source code
COPY . .

# Make react-scripts executable (important!)
RUN chmod +x ./node_modules/.bin/react-scripts

# Build the React app
RUN npm run build
# OR: RUN npx react-scripts build (both work now)

# Stage 2: Serve with Nginx
FROM nginx:stable-alpine

# Copy the build output to Nginx's html folder
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 (Nginx default) instead of 3000
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
