import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { componentRegistry } from "./quartz/components/registry"
import type { ExplorerOptions } from "@quartz-community/explorer"

// Record overrides before loadQuartzConfig instantiates the Explorer component.
// Keep rank/page literals inside the callbacks because Explorer serializes them for the browser.
const explorerOptions: Partial<ExplorerOptions> = {
  title: "Projects",
  folderDefaultState: "open",
  folderClickBehavior: "link",
  useSavedState: false,
  sortFn: (a, b) => {
    const ranks: Record<string, number> = {"apollo-system": 3.0, "dactyl-manuform": 2.0, "file-drive": 1.0, "home-server": 0.0, "index": -1e+300, "zenflix": 4.0}
    const aSlug = String(a.data?.slug ?? a.slugSegments?.join("/") ?? "")
    const bSlug = String(b.data?.slug ?? b.slugSegments?.join("/") ?? "")
    const aRank = ranks[aSlug] ?? 1e100
    const bRank = ranks[bSlug] ?? 1e100
    return aRank - bRank || (a.displayName ?? "").localeCompare(b.displayName ?? "", undefined, { numeric: true, sensitivity: "base" })
  },
  filterFn: (node) => {
    const pages: string[] = ["index", "apollo-system", "dactyl-manuform", "file-drive", "home-server", "zenflix"]
    const key = String(node.data?.slug ?? node.slugSegments?.join("/") ?? "")
    return pages.includes(key)
  },
}
componentRegistry.setOptionOverrides("@quartz-community/explorer", explorerOptions)

const config = await loadQuartzConfig()
export default config
export const layout = await loadQuartzLayout()
