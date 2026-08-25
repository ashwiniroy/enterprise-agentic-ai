import {
  Paper,
  Typography,
  CircularProgress
} from "@mui/material";

const AIResponsePanel = ({
  response,
  loading
}) => {

  return (
    <Paper sx={{ p: 3 }}>
      <Typography variant="h6" mb={2}>
        AI Response
      </Typography>

      {loading ? (
        <CircularProgress />
      ) : (
        <Typography whiteSpace="pre-wrap">
          {response || "Ask a question to begin."}
        </Typography>
      )}
    </Paper>
  );
};

export default AIResponsePanel;