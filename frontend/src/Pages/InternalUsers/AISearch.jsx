import React from "react";
import { Box, Grid, Typography } from "@mui/material";

import AIInputPanel from "../../Components/ai/AIInputPanel";
import AIResponsePanel from "../../Components/ai/AIResponsePanel";
import SuggestedQuestions from "../../Components/ai/SuggestedQuestions";

import { askAI } from "../../Services/ai/SearchQuery";

const AISearch = () => {
  const [query, setQuery] = React.useState("");
  const [response, setResponse] = React.useState("");
  const [loading, setLoading] = React.useState(false);

  const handleAskAI = async () => {
    if (!query.trim()) return;

    try {
      setLoading(true);

      const result = await askAI(query);

      setResponse(result.answer); // adjust according to API response
    } catch (err) {
      console.error(err);
      setResponse("Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box>
      <Typography variant="h4" fontWeight={700} mb={4}>
        AI Review Assistant
      </Typography>

      <Grid container spacing={3}>
        <Grid size={{ xs: 12, md: 4 }}>
          <AIInputPanel
            query={query}
            setQuery={setQuery}
            onClick={handleAskAI}
            loading={loading}
          />

          <SuggestedQuestions />
        </Grid>

        <Grid size={{ xs: 12, md: 8 }}>
          <AIResponsePanel
            response={response}
            loading={loading}
          />
        </Grid>
      </Grid>
    </Box>
  );
};

export default AISearch;