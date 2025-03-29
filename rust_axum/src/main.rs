use axum::{
    extract::DefaultBodyLimit,
    routing::{get, post},
    Router,
    http::StatusCode,
    response::Json,
    body::Bytes,
};
use std::net::SocketAddr;
use zune_jpeg::JpegDecoder;

#[tokio::main]
async fn main() {
    // Create our router with the routes
    let app = Router::new()
        .route("/healthcheck/", get(healthcheck))
        .route("/test/", post(test))
        // Set a reasonable body size limit
        .layer(DefaultBodyLimit::max(10 * 1024 * 1024)); // 10MB limit

    // Run the server
    // get environment variable for port
    let port = std::env::var("API_PORT").unwrap_or_else(|_| "8080".to_string());
    let addr = SocketAddr::from(([0, 0, 0, 0], port.parse::<u16>().unwrap()));
    println!("Server running on http://{}", addr);
    let listener = tokio::net::TcpListener::bind(&addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();

    // let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap();
    // axum::serve(listener, app).await.unwrap();
}

// Handler for GET /healthcheck/
async fn healthcheck() -> Json<serde_json::Value> {
    Json(serde_json::json!({
        "Status": 1
    }))
}

// Handler for POST /test/
async fn test(body: Bytes) -> (StatusCode, Json<serde_json::Value>) {
    // Create a JPEG decoder
    let mut decoder = JpegDecoder::new(&body[..]);

    // Decode the JPEG headers to get dimensions
    if let Err(e) = decoder.decode_headers() {
        return (
            StatusCode::BAD_REQUEST,
            Json(serde_json::json!({
                "error": format!("Failed to decode JPEG headers: {}", e)
            }))
        );
    }

    // let mut decoder = JpegDecoder::new(&[]);
    decoder.decode_headers().unwrap();
    let image_info = decoder.info().unwrap();
    // println!("{},{}",image_info.width,image_info.height)

    // Get the image dimensions
    let height = image_info.height as usize;
    let width = image_info.width as usize;
    // let channels = decoder.components() as usize;

    // Return the shape information as JSON
    (
        StatusCode::OK,
        Json(serde_json::json!({
            "shape": [height, width, 3]
        }))
    )
}