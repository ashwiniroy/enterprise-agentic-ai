import { Box, Grid, Typography } from "@mui/material";

import AppButton from "../../Components/Common/Button";

import UserProfileCard from "../../Components/Settings/UserProfileCard";
import NotificationCard from "../../Components/Settings/NotificationCard";
import AIConfigurationCard from "../../Components/Settings/AIConfigurationCard";
import ApplicationSettingsCard from "../../Components/Settings/ApplicationSettingsCard";

const Settings = () => {
  return (
    <Box>

      <Typography
        variant="h4"
        fontWeight={700}
        mb={1}
      >
        Settings
      </Typography>

      <Typography
        color="text.secondary"
        mb={4}
      >
        Manage application preferences and AI configuration
      </Typography>

      <Grid container spacing={3}>

        <Grid size={{ xs: 12, md: 6 }}>
          <UserProfileCard />
        </Grid>

        <Grid size={{ xs: 12, md: 6 }}>
          <NotificationCard />
        </Grid>

        <Grid size={{ xs: 12, md: 6 }}>
          <AIConfigurationCard />
        </Grid>

        <Grid size={{ xs: 12, md: 6 }}>
          <ApplicationSettingsCard />
        </Grid>

      </Grid>

      <Box
        display="flex"
        justifyContent="flex-end"
        gap={2}
        mt={4}
      >
        <AppButton variant="outlined">
          Cancel
        </AppButton>

        <AppButton>
          Save Changes
        </AppButton>
      </Box>

    </Box>
  );
};

export default Settings;