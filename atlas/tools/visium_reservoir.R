# Export avijgan2026br's Visium sections. Uses DIRECT SLOT ACCESS, not Seurat
# functions: SeuratObject alone can hold the object, and GetAssayData lives in
# Seurat, which is a much heavier dependency and is not needed to read counts.
suppressWarnings(suppressMessages(library(SeuratObject)))
args <- commandArgs(trailingOnly=TRUE)
indir  <- args[1]; outdir <- if (length(args)>1) args[2] else "visium_export"
dir.create(outdir, showWarnings=FALSE)
files <- list.files(indir, pattern="\\.rds$", full.names=TRUE)
cat("sections found:", length(files), "\n")
for (f in files) {
  nm <- tools::file_path_sans_ext(basename(f))
  o <- tryCatch(readRDS(f), error=function(e){cat(" FAIL",nm,conditionMessage(e),"\n"); NULL})
  if (is.null(o)) next
  md <- o@meta.data
  a  <- o@assays[["Spatial"]]
  if (is.null(a)) a <- o@assays[[1]]
  m <- NULL
  if (.hasSlot(a,"counts")) m <- a@counts
  if ((is.null(m) || !length(m)) && .hasSlot(a,"layers")) {
    L <- a@layers; k <- grep("^counts", names(L), value=TRUE)
    if (length(k)) m <- L[[k[1]]]
  }
  if (is.null(m) || !length(m)) { cat(" ",nm,"no counts found\n"); next }
  gn <- if (.hasSlot(a,"features")) rownames(a@features) else rownames(m)
  cn <- if (.hasSlot(a,"cells")) rownames(a@cells) else colnames(m)
  if (is.null(gn)) gn <- rownames(m); if (is.null(cn)) cn <- colnames(m)
  # spot coordinates, if an image is attached
  coords <- NULL
  if (length(o@images)) {
    im <- o@images[[1]]
    if (.hasSlot(im,"coordinates")) coords <- im@coordinates
  }
  write.csv(md, file.path(outdir,paste0(nm,".meta.csv")))
  Matrix::writeMM(m, file.path(outdir,paste0(nm,".counts.mtx")))
  write.csv(data.frame(x=gn), file.path(outdir,paste0(nm,".genes.csv")), row.names=FALSE)
  write.csv(data.frame(x=cn), file.path(outdir,paste0(nm,".spots.csv")), row.names=FALSE)
  if (!is.null(coords)) write.csv(coords, file.path(outdir,paste0(nm,".coords.csv")))
  areas <- if ("area" %in% colnames(md)) paste(names(table(md$area)), table(md$area), sep="=", collapse=" ") else "no area column"
  cat(sprintf("  %-22s %6d spots x %5d genes | %s\n", nm, ncol(m), nrow(m), areas))
}
