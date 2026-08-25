import {
    Card,
    CardContent,
    Typography,
    Grid,
    Slider
  } from "@mui/material";
  
  import AppSelect from "../../Components/Common/AppSelect";
  import AppInput from "../../Components/Common/Input";
  
  const AIConfigurationCard = () => {
    return (
      <Card>
  
        <CardContent>
  
          <Typography variant="h6" mb={3}>
            AI Configuration
          </Typography>
  
          <Grid container spacing={2}>
  
            <Grid size={{ xs: 12 }}>
              <AppSelect
                label="LLM Model"
                value=""
                options={[
                  { value: "gpt-4.1", label: "GPT-4.1" },
                  { value: "gpt-5", label: "GPT-5" },
                  { value: "claude", label: "Claude" }
                ]}
              />
            </Grid>
  
            <Grid size={{ xs: 12 }}>
              <Typography gutterBottom>
                Temperature
              </Typography>
  
              <Slider
                defaultValue={0.7}
                min={0}
                max={1}
                step={0.1}
              />
            </Grid>
  
            <Grid size={{ xs: 12 }}>
              <AppInput
                label="Max Tokens"
                value="2048"
              />
            </Grid>
  
          </Grid>
  
        </CardContent>
  
      </Card>
    );
  };
  
  export default AIConfigurationCard;