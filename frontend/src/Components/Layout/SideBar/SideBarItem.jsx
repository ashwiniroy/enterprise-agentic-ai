import {
    ListItemButton,
    ListItemIcon,
    ListItemText,
  } from "@mui/material";
  
  import { NavLink } from "react-router-dom";
  
  const SidebarItem = ({ item }) => {
    return (
      <ListItemButton
        component={NavLink}
        to={item.path}
        sx={{
          borderRadius: 2,
          mb: 1,
          "&.active": {
            backgroundColor: "primary.main",
            color: "#fff",
          },
          "&.active .MuiListItemIcon-root": {
            color: "#fff",
          },
        }}
      >
        <ListItemIcon>{item.icon}</ListItemIcon>
  
        <ListItemText primary={item.title} />
      </ListItemButton>
    );
  };
  
  export default SidebarItem;