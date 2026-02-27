# build stage
FROM node:22-alpine

WORKDIR /app

# install dependencies
RUN npm install -g pnpm

# copy dependency files first
COPY package.json pnpm-lock.yaml ./

RUN pnpm install

# Copy rest of frontend code
COPY . .

# Expose port 5173 for webapp
EXPOSE 5173

CMD ["pnpm", "run", "dev", "--host"]