import {
    AppBar,
    Toolbar,
    Typography,
    Box,
    IconButton,
    Avatar,
  } from "@mui/material";
  
  import NotificationsIcon from "@mui/icons-material/Notifications";
  
  const Navbar = () => {
    return (
      <AppBar
        position="fixed"
        color="inherit"
        elevation={1}
        sx={{
          ml: "260px",
          width: "calc(100% - 260px)",
        }}
      >
        <Toolbar>
          <Typography variant="h6">
            Review Analysis Platform
          </Typography>
  
          <Box flexGrow={1} />
  
          <IconButton>
            <NotificationsIcon />
          </IconButton>
  
          <Avatar sx={{ ml: 2 }}>
            A
          </Avatar>
        </Toolbar>
      </AppBar>
    );
  };
  
  export default Navbar;