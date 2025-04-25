document.getElementById("grant-form").addEventListener("submit", async e => {
    e.preventDefault();
    const form = e.target;
    const data = new FormData(form);
    try {
      const resp = await fetch("/generate", {
        method: "POST",
        body: data
      });
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      const blob = await resp.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "updated.docx";
      a.click();
      URL.revokeObjectURL(url);
    } catch (err) {
      alert("Error: " + err.message);
    }
  });
  