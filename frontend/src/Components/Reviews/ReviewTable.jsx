import { DataGrid } from "@mui/x-data-grid";
import Rating from "@mui/material/Rating";
import Chip from "@mui/material/Chip";

import ReviewStatusChip from "./ReviewStatusChip";
import ReviewActionButtons from "./ReviewActionButton";

const columns = [
  {
    field: "customerName",
    headerName: "Customer",
    flex: 1.3,
  },
  {
    field: "product",
    headerName: "Product",
    flex: 1,
  },
  {
    field: "category",
    headerName: "Category",
    flex: 1,
  },
  {
    field: "rating",
    headerName: "Rating",
    flex: 1,
    renderCell: (params) => (
      <Rating
        value={params.value}
        readOnly
        size="small"
      />
    ),
  },
  {
    field: "sentiment",
    headerName: "Sentiment",
    flex: 1,
    renderCell: (params) => (
      <Chip
        label={params.value}
        color={
          params.value === "Positive"
            ? "success"
            : params.value === "Negative"
            ? "error"
            : "warning"
        }
        size="small"
      />
    ),
  },
  {
    field: "status",
    headerName: "Status",
    flex: 1,
    renderCell: (params) => (
      <ReviewStatusChip status={params.value} />
    ),
  },
  {
    field: "createdDate",
    headerName: "Created",
    flex: 1,
  },
  {
    field: "actions",
    headerName: "Actions",
    sortable: false,
    filterable: false,
    flex: 1.2,
    renderCell: () => <ReviewActionButtons />,
  },
];

const ReviewTable = ({ rows }) => {
  return (
    <DataGrid
      rows={rows}
      columns={columns}
      disableRowSelectionOnClick
      pageSizeOptions={[5, 10, 20]}
      initialState={{
        pagination: {
          paginationModel: {
            pageSize: 5,
          },
        },
      }}
    />
  );
};

export default ReviewTable;