# AlphaPredict - Stock Price Prediction Website

AlphaPredict is a web application designed to provide stock price predictions. Built using React, Express, and MongoDB, this project offers users insights into potential stock price trends.

## How to Run

To run the AlphaPredict project, follow these steps:


### Frontend

1. Navigate to the "frontend" directory:
   ```
   cd frontend
   ```

2. Install the frontend dependencies:
   ```
   npm install
   ```

3. Create a `.env` file in the "frontend" directory and add your Finnhub API key:
   ```
   REACT_APP_API_KEY="YOUR_API_KEY"
   ```

   Obtain the API key from [Finnhub](https://finnhub.io/).

4. Start the frontend development server:
   ```
   npm start
   ```

### Backend

1. Navigate to the "backend" directory:
   ```
   cd backend
   ```

2. Install the backend dependencies:
   ```
   npm install
   ```

3. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the "backend" directory and add the following:
   ```
   ATLAS_DATABASE_USERNAME=YOUR_USERNAME
   ATLAS_DATABASE_PASSWORD=YOUR_PASSWORD
   SECRET=YOUR_SECRET
   ```

   Obtain your Atlas Database username and password. Make sure to allow the server machine's IP and set a random SECRET for security.

5. Start the backend server:
   ```
   npm start
   ```

The frontend will run on `localhost:3000`, and the backend will run on `localhost:5000`.

