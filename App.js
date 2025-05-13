import React from "react";
import { BrowserRouter as Router, Route, Routes, Navigate } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import AdminDashboard from "./pages/AdminDashboard";
import DoctorDashboard from "./pages/DoctorDashboard";
import NurseDashboard from "./pages/NurseDashboard";
import LabDashboard from "./pages/LabDashboard";
import PatientDashboard from "./pages/PatientDashboard";
import PharmacistDashboard from "./pages/PharmacistDashboard";
import AccountantDashboard from "./pages/AccountantDashboard";
import NotFound from "./pages/NotFound";

const getUserRole = () => {
  const token = localStorage.getItem("token");
  const role = localStorage.getItem("role");
  return token ? role : null;
};

function App() {
  const role = getUserRole();

  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route
          path="/dashboard"
          element={
            role === "admin" ? (
              <AdminDashboard />
            ) : role === "doctor" ? (
              <DoctorDashboard />
            ) : role === "nurse" ? (
              <NurseDashboard />
            ) : role === "lab" ? (
              <LabDashboard />
            ) : role === "pharmacist" ? (
              <PharmacistDashboard />
            ) : role === "accountant" ? (
              <AccountantDashboard />
            ) : role === "patient" ? (
              <PatientDashboard />
            ) : (
              <Navigate to="/" />
            )
          }
        />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
}

export default App;
