"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g = Object.create((typeof Iterator === "function" ? Iterator : Object).prototype);
    return g.next = verb(0), g["throw"] = verb(1), g["return"] = verb(2), typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
// Example 1: read a file synchronously
var contents = fs.readFileSync("notes.txt", "utf-8");
console.log(contents);
// Example 2: write to a file synchronously
fs.writeFileSync("output.txt", "Hello from TypeScript!\n");
fs.appendFileSync("output.txt", "Appending a new line.\n");
fs.appendFileSync("another_output.txt", "This is another file.\n");
// Example 3. Async File I/O (Very Important)
fs.readFile("notes.txt", "utf-8", function (err, data) {
    if (err) {
        console.error("Error reading file:", err);
        return;
    }
    console.log(data);
});
//writing asynchronously
fs.writeFile("async_output.txt", "Async write\n", function (err) {
    if (err) {
        console.error("Error writing file:", err);
    }
});
// Example 4. Promise-based API (Best Modern Style)
var promises_1 = require("fs/promises");
function run() {
    return __awaiter(this, void 0, void 0, function () {
        var data;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0: return [4 /*yield*/, (0, promises_1.writeFile)("data.txt", "Saved using promises\n")];
                case 1:
                    _a.sent();
                    return [4 /*yield*/, (0, promises_1.readFile)("data.txt", "utf-8")];
                case 2:
                    data = _a.sent();
                    console.log(data);
                    return [2 /*return*/];
            }
        });
    });
}
run();
// Example 5. JSON Files (Extremely Common)
// writing JSON
// import { writeFile, readFile } from "fs/promises"; // already imported above
function saveApplication() {
    return __awaiter(this, void 0, void 0, function () {
        var application;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    application = {
                        company: "Tech Corp",
                        applicationsSent: 12,
                        response: true,
                    };
                    return [4 /*yield*/, (0, promises_1.writeFile)("application.json", JSON.stringify(application, null, 2), "utf-8")];
                case 1:
                    _a.sent();
                    return [2 /*return*/];
            }
        });
    });
}
saveApplication();
// reading JSON
function readApplication() {
    return __awaiter(this, void 0, void 0, function () {
        var raw, data;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0: return [4 /*yield*/, (0, promises_1.readFile)("application.json", "utf-8")];
                case 1:
                    raw = _a.sent();
                    console.log("Raw JSON string:", raw);
                    if (!raw.trim()) {
                        console.log("JSON file is empty");
                        return [2 /*return*/];
                    }
                    data = JSON.parse(raw);
                    console.log(data);
                    return [2 /*return*/];
            }
        });
    });
}
readApplication();
// Example 6. Paths (Cross-Platform Safe)
var path = require("path");
var filePath = path.join("data", "files", "log.txt");
console.log("Cross-platform file path:", filePath);
