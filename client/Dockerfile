# Use an official Node.js runtime as a parent image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json into the container at /app
COPY package*.json ./

# Install npm dependencies
RUN npm install

# Copy the rest of the application's code into the container at /app
COPY . .

# Expose port 3000 to the outside world
EXPOSE 3000

# Run the React client when the container launches
CMD ["npm", "start"]
