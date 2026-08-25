import {
    Box,
    Toolbar,
  } from "@mui/material";
  
  import { Outlet } from "react-router-dom";
  
  import Sidebar from "../Components/Layout/SideBar/Sidebar";
  import Navbar from "../Components/Layout/SideBar/Navbar";
  
  const drawerWidth = 260;
  
  const MainLayout = () => {
    return (
      <Box display="flex">
  
        <Navbar />
  
        <Sidebar />
  
        <Box
          component="main"
          sx={{
            flexGrow: 1,
            bgcolor: "background.default",
            p: 4,
            ml: `${drawerWidth}px`,
          }}
        >
          <Toolbar />
  
          <Outlet />
  
        </Box>
  
      </Box>
    );
  };
  
  export default MainLayout;