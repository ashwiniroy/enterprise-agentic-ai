import { Card, CardContent, Typography, Grid } from "@mui/material";

import AppInput from "../../Components/Common/Input";

const UserProfileCard = () => {
  return (
    <Card>
      <CardContent>

        <Typography variant="h6" mb={3}>
          User Profile
        </Typography>

        <Grid container spacing={2}>

          <Grid size={{ xs: 12 }}>
            <AppInput
              label="Full Name"
              value="Ashwini Kumar"
            />
          </Grid>

          <Grid size={{ xs: 12 }}>
            <AppInput
              label="Email"
              value="ashwini@gmail.com"
            />
          </Grid>

          <Grid size={{ xs: 12 }}>
            <AppInput
              label="Role"
              value="Administrator"
            />
          </Grid>

        </Grid>

      </CardContent>
    </Card>
  );
};

export default UserProfileCard;