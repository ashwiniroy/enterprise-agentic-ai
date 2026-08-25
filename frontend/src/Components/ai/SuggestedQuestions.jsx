import { Paper, Typography, Stack, Chip } from "@mui/material";

const questions = [
  "Summarize all reviews",
  "Show negative reviews",
  "Compare products",
  "Top customer complaints",
  "Products with highest ratings",
  "Reviews about battery"
];

const SuggestedQuestions = () => {
  return (
    <Paper sx={{ p: 3, mt: 3 }}>
      <Typography variant="h6" mb={2}>
        Suggested Questions
      </Typography>

      <Stack spacing={1}>
        {questions.map((q) => (
          <Chip
            key={q}
            label={q}
            clickable
            variant="outlined"
          />
        ))}
      </Stack>
    </Paper>
  );
};

export default SuggestedQuestions;