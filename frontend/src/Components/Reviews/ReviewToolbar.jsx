import { Paper, Grid } from "@mui/material";

import SearchBar from "../Common/SearchBar";
import AppSelect from "../../Components/Common/AppSelect";
import AppButton from "../Common/Button";

const ReviewToolbar = () => {
  return (
    <Paper sx={{ p: 3, mb: 3 }}>
      <Grid container spacing={2}>

        <Grid size={{ xs: 12, md: 4 }}>
          <SearchBar placeholder="Search Reviews..." />
        </Grid>

        <Grid size={{ xs: 12, md: 2 }}>
          <AppSelect
            label="Product"
            value=""
            options={[]}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 2 }}>
          <AppSelect
            label="Sentiment"
            value=""
            options={[]}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 2 }}>
          <AppSelect
            label="Status"
            value=""
            options={[]}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 2 }}>
          <AppButton fullWidth variant="outlined">
            Reset
          </AppButton>
        </Grid>

      </Grid>
    </Paper>
  );
};

export default ReviewToolbar;