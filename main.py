import UI
import WebpageParsing
SearchBar = UI.TitleEntry()
ParsingScript = WebpageParsing.Siddhater()
SearchBar.SearchUI()
ParsingScript.search(SearchBar.SearchEntry)