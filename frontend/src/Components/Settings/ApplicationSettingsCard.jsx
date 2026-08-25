import {
    Card,
    CardContent,
    Typography,
    Grid
  } from "@mui/material";
  
  import AppSelect from "../../Components/Common/AppSelect";
  
  const ApplicationSettingsCard = () => {
    return (
      <Card>
  
        <CardContent>
  
          <Typography variant="h6" mb={3}>
            Application Settings
          </Typography>
  
          <Grid container spacing={2}>
  
            <Grid size={{ xs: 12 }}>
              <AppSelect
                label="Theme"
                value=""
                options={[
                  { value: "light", label: "Light" },
                  { value: "dark", label: "Dark" }
                ]}
              />
            </Grid>
  
            <Grid size={{ xs: 12 }}>
              <AppSelect
                label="Language"
                value=""
                options={[
                  { value: "en", label: "English" },
                  { value: "hi", label: "Hindi" }
                ]}
              />
            </Grid>
  
            <Grid size={{ xs: 12 }}>
              <AppSelect
                label="Date Format"
                value=""
                options={[
                  {
                    value: "dd-mm-yyyy",
                    label: "DD-MM-YYYY"
                  },
                  {
                    value: "mm-dd-yyyy",
                    label: "MM-DD-YYYY"
                  }
                ]}
              />
            </Grid>
  
          </Grid>
  
        </CardContent>
  
      </Card>
    );
  };
  
  export default ApplicationSettingsCard;