import {
    Card,
    CardContent,
    Typography,
    FormGroup,
    FormControlLabel,
    Checkbox
  } from "@mui/material";
  
  const NotificationCard = () => {
    return (
      <Card>
        <CardContent>
  
          <Typography variant="h6" mb={2}>
            Notifications
          </Typography>
  
          <FormGroup>
  
            <FormControlLabel
              control={<Checkbox defaultChecked />}
              label="Email Notifications"
            />
  
            <FormControlLabel
              control={<Checkbox defaultChecked />}
              label="AI Analysis Complete"
            />
  
            <FormControlLabel
              control={<Checkbox />}
              label="Weekly Reports"
            />
  
          </FormGroup>
  
        </CardContent>
      </Card>
    );
  };
  
  export default NotificationCard;