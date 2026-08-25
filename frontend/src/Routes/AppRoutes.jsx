import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import MainLayout from "../Layouts/MainLayout";

import Dashboard from "../Pages/InternalUsers/Dashboard";
import Reviews from "../Pages/Customers/Reviews";
import CreateReview from "../Pages/Customers/CreateReview";
import Analytics from "../Pages/InternalUsers/Analytics";
import AISearch from "../Pages/InternalUsers/AISearch";
import Settings from "../Pages/Common/Settings";

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>

                <Route element={<MainLayout />}>

                    <Route
                        path="/"
                        element={<Navigate to="/dashboard" />}
                    />

                    <Route
                        path="/dashboard"
                        element={<Dashboard />}
                    />

                    <Route
                        path="/reviews"
                        element={<Reviews />}
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
                        element={<AISearch />}
                    />

                    <Route
                        path="/settings"
                        element={<Settings />}
                    />

                </Route>

            </Routes>
        </BrowserRouter>
    );
};

export default AppRoutes;