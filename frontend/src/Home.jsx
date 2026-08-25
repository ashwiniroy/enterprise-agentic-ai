import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import CreateReview from "./Pages/Customers/CreateReview";
import Dashboard from "./Pages/InternalUsers/Dashboard";
import MainLayout from "./Layouts/MainLayout";
import Analytics from "./Pages/InternalUsers/Analytics";
import AISearch from "./Pages/InternalUsers/AISearch"
import Settings from "./Pages/Common/Settings"
import Reviews from "./Pages/Customers/Reviews";

function Home() {
  return (
    <Router>
      <Routes>

<Route element={<MainLayout />}>

    <Route
        path="/dashboard"
        element={<Dashboard />}
    />

    <Route
        path="/reviews"
        element={<Reviews/>}
    />

    <Route
        path="/create-review"
        element={<CreateReview />}
    />

    <Route
        path="/analytics"
        element={<Analytics />}
    />

    <Route
        path="/ai-search"
        element={<AISearch/>}
    />

    <Route
        path="/settings"
        element={<Settings/>}
    />

</Route>

</Routes>
    </Router>
  );
}

export default Home;