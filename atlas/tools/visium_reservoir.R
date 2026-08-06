# Read avijgan2026br's Visium sections and pseudobulk the Hedgehog/stromal panel
# by annotated area. Standard Visium spots carry far more depth than the
# bin2cell-segmented Visium HD object, in which GLI1 had 21 counts in an entire
# section and the analysis was refused.
#
# This script only EXPORTS. All guards and all interpretation stay in Python so
# that the pre-registered checks are applied in one place.
suppressWarnings(suppressMessages({ ok <- require(Seurat, quietly=TRUE) }))
args <- commandArgs(trailingOnly=TRUE)
outdir <- if (length(args)>1) args[2] else "visium_export"
dir.create(outdir, showWarnings=FALSE)
files <- list.files(args[1], pattern="\\.rds$", full.names=TRUE)
cat("sections found:", length(files), "\n")
for (f in files) {
  nm <- tools::file_path_sans_ext(basename(f))
  o <- tryCatch(readRDS(f), error=function(e){cat("  FAIL", nm, conditionMessage(e), "\n"); NULL})
  if (is.null(o)) next
  cat("\n===", nm, "| class:", class(o)[1], "\n")
  if (inherits(o, "Seurat")) {
    cat("  assays:", paste(names(o@assays), collapse=", "), "\n")
    cat("  meta cols:", paste(colnames(o@meta.data), collapse=", "), "\n")
    cat("  n spots:", ncol(o), " n features:", nrow(o), "\n")
    for (cc in colnames(o@meta.data)) {
      v <- o@meta.data[[cc]]
      if ((is.factor(v) || is.character(v)) && length(unique(v)) <= 12) {
        cat("   ", cc, ":", paste(names(table(v)), table(v), sep="=", collapse=" "), "\n")
      }
    }
    a <- names(o@assays)[1]
    m <- tryCatch(Seurat::GetAssayData(o, assay=a, layer="counts"), error=function(e) NULL)
    if (is.null(m)) m <- tryCatch(Seurat::GetAssayData(o, assay=a, slot="counts"), error=function(e) NULL)
    if (!is.null(m)) {
      write.csv(as.matrix(o@meta.data), file.path(outdir, paste0(nm,".meta.csv")))
      Matrix::writeMM(m, file.path(outdir, paste0(nm,".counts.mtx")))
      write.csv(rownames(m), file.path(outdir, paste0(nm,".genes.csv")), row.names=FALSE)
      write.csv(colnames(m), file.path(outdir, paste0(nm,".spots.csv")), row.names=FALSE)
      cat("  exported counts", nrow(m), "x", ncol(m), "\n")
    }
  } else {
    cat("  not a Seurat object; names:", paste(utils::head(names(o),20), collapse=", "), "\n")
  }
}
