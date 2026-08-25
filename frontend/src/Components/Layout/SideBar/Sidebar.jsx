import {
    Drawer,
    Toolbar,
    List,
    Box,
  } from "@mui/material";
  
  import { navigationItems } from "../../../Constants/navigation";
  import SidebarItem from "./SideBarItem";
  import Logo from "../Logo";
  
  const drawerWidth = 260;
  
  const Sidebar = () => {
    return (
      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
  
          "& .MuiDrawer-paper": {
            width: drawerWidth,
            boxSizing: "border-box",
            borderRight: "1px solid #E5E7EB",
          },
        }}
      >
        <Toolbar>
          <Logo />
        </Toolbar>
  
        <Box p={2}>
          <List>
            {navigationItems.map((item) => (
              <SidebarItem
                key={item.path}
                item={item}
              />
            ))}
          </List>
        </Box>
      </Drawer>
    );
  };
  
  export default Sidebar;